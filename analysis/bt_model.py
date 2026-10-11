"""Time-decayed, regularized Bradley-Terry map model:
logit P(A beats B on map m) = (th_A + ph_Am) - (th_B + ph_Bm)
Fitted on every map result in the fetched tournament pages (all teams)."""
import json, os, math, datetime, collections
import numpy as np
D = os.path.dirname(os.path.abspath(__file__)) + '/work/'
raw = json.load(open(D + 'all_matches_raw.json'))
ALIAS = {'vit': 'vitality', 'team vitality': 'vitality', 'mousesports': 'mouz'}
def norm(o): return ALIAS.get(o, o)

def rows(start='2025-10-01', end='2026-10-10'):
    seen = set(); out = []
    for m in raw:
        if not m['date'] or not (start <= m['date'] <= end): continue
        a, b = norm(m['o1']), norm(m['o2'])
        if not a or not b or a == b or 'tbd' in (a, b): continue
        for i, mp in enumerate(m['maps']):
            if mp['finished'] in ('skip', '') or mp['s1'] is None or mp['s1'] == mp['s2']: continue
            name = mp['map'].replace('Dust II', 'Dust2')
            key = (m['date'], a, b, i, name, mp['s1'], mp['s2'])
            if key in seen: continue
            seen.add(key)
            out.append((m['date'], a, b, name, 1 if mp['s1'] > mp['s2'] else 0, mp['s1'], mp['s2']))
    return out

def fit(data, ref_date, half_life=120, lam_t=0.05, lam_m=1.0, iters=25):
    """Penalized weighted logistic regression solved by Newton-Raphson."""
    teams = sorted({r[1] for r in data} | {r[2] for r in data})
    maps = sorted({r[3] for r in data})
    ti = {t: i for i, t in enumerate(teams)}; mi = {m: i for i, m in enumerate(maps)}
    T, M = len(teams), len(maps)
    P = T + T * M
    ref = datetime.date.fromisoformat(ref_date)
    n = len(data)
    X = np.zeros((n, P))
    for k, r in enumerate(data):
        a, b, m = ti[r[1]], ti[r[2]], mi[r[3]]
        X[k, a] += 1; X[k, b] -= 1
        X[k, T + a * M + m] += 1; X[k, T + b * M + m] -= 1
    y = np.array([r[4] for r in data], float)
    age = np.array([(ref - datetime.date.fromisoformat(r[0])).days for r in data], float)
    w = 0.5 ** (np.maximum(age, 0) / half_life)
    lam = np.concatenate([np.full(T, lam_t), np.full(T * M, lam_m)])
    beta = np.zeros(P)
    for it in range(iters):
        z = X @ beta
        p = 1 / (1 + np.exp(-z))
        g = X.T @ (w * (p - y)) + lam * beta
        Wd = w * p * (1 - p)
        H = (X * Wd[:, None]).T @ X + np.diag(lam)
        step = np.linalg.solve(H, g)
        beta -= step
        if np.abs(step).max() < 1e-6: break
    th = beta[:T]; ph = beta[T:].reshape(T, M)
    return dict(th=th, ph=ph, ti=ti, mi=mi, teams=teams, maps=maps, H=H, beta=beta, T=T, M=M)

def prob(model, a, b, mp):
    ti, mi = model['ti'], model['mi']
    z = model['th'][ti[a]] - model['th'][ti[b]]
    if mp in mi:
        z += model['ph'][ti[a], mi[mp]] - model['ph'][ti[b], mi[mp]]
    return 1 / (1 + math.exp(-z))

def backtest(half_life, lam_t, lam_m, cut_dates):
    """Fit on data before each cut date, score maps in [cut, next cut)."""
    data = rows('2025-06-01', '2026-10-10')
    ll = 0; n = 0; correct = 0
    for i, c in enumerate(cut_dates[:-1]):
        train = [r for r in data if r[0] < c]
        test = [r for r in data if c <= r[0] < cut_dates[i + 1]]
        mdl = fit(train, c, half_life, lam_t, lam_m)
        for r in test:
            if r[1] not in mdl['ti'] or r[2] not in mdl['ti']: continue
            p = min(max(prob(mdl, r[1], r[2], r[3]), 1e-4), 1 - 1e-4)
            ll += -(r[4] * math.log(p) + (1 - r[4]) * math.log(1 - p)); n += 1
            correct += (p > 0.5) == (r[4] == 1)
    return ll / n, correct / n, n

if __name__ == '__main__':
    import sys
    cuts = ['2026-03-01', '2026-04-10', '2026-05-08', '2026-06-01', '2026-07-20', '2026-08-25', '2026-09-15', '2026-10-01', '2026-10-11']
    best = None
    for hl in [45, 90, 180]:
        for lt in [0.3, 1.0, 3.0]:
            for lm in [3.0, 10.0, 30.0]:
                ll, acc, n = backtest(hl, lt, lm, cuts)
                print(f"half_life={hl:3d} lam_team={lt:<5} lam_map={lm:<4} logloss={ll:.4f} acc={acc:.3f} n={n}")
                if best is None or ll < best[0]: best = (ll, hl, lt, lm)
    print('BEST', best)
    json.dump({'best': best}, open(D + 'bt_best.json', 'w'))
