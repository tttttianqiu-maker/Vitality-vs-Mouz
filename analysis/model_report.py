"""Fit final models, backtest, and write model_results.json."""
import sys, os, json, math
from itertools import product
from math import comb
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import bt_model as b
OUT = sys.argv[1]
CUTS = ['2026-03-01', '2026-04-10', '2026-05-08', '2026-06-01', '2026-07-20', '2026-08-25', '2026-09-15', '2026-10-01', '2026-10-11']
data = b.rows('2025-06-01', '2026-10-10')

def relabel(rows):
    out = []
    for d, a, bb, m, y, s1, s2 in rows:
        lab = lambda t: 'mouz_pre' if (t == 'mouz' and d < '2026-07-14') else ('vitality_jl' if (t == 'vitality' and '2026-08-26' <= d <= '2026-09-06') else t)
        out.append((d, lab(a), lab(bb), m, y, s1, s2))
    return out

def bo5(p): return sum(comb(2 + k, k) * p ** 3 * (1 - p) ** k for k in range(3))

def series_dist(ps):
    dist = {}
    for outcome in product([1, 0], repeat=5):
        pr = 1.0
        for o, p in zip(outcome, ps): pr *= p if o else 1 - p
        v = m = 0
        for o in outcome:
            v += o; m += 1 - o
            if v == 3 or m == 3: break
        dist[f'{v}-{m}'] = dist.get(f'{v}-{m}', 0) + pr
    return dist

res = {'dataset': {'map_results_used': len(data), 'teams': len({r[1] for r in data} | {r[2] for r in data}),
                   'window': '2025-06-01..2026-10-10', 'source': 'Liquipedia match2 records of every tournament Vitality or MOUZ played since May 2024'}}
# backtest of chosen config (team strength only) + map-aware config
bt = {}
for name, lm in [('team_strength_only', 1e4), ('map_aware_lam30', 30.0), ('map_aware_lam3', 3.0)]:
    ll, acc, n = b.backtest(180, 3.0, lm, CUTS)
    bt[name] = {'logloss': round(ll, 4), 'accuracy': round(acc, 4), 'n_maps': n}
bt['coin_flip_logloss'] = round(math.log(2), 4)
res['backtest'] = bt
# calibration for chosen config
preds = []
for i, c in enumerate(CUTS[:-1]):
    train = [r for r in data if r[0] < c]; test = [r for r in data if c <= r[0] < CUTS[i + 1]]
    mdl = b.fit(train, c, 180, 3.0, 1e4)
    for r in test:
        if r[1] in mdl['ti'] and r[2] in mdl['ti']:
            p = b.prob(mdl, r[1], r[2], r[3]); preds.append((max(p, 1 - p), r[4] if p >= 0.5 else 1 - r[4]))
cal = []
for lo, hi in [(0.5, 0.55), (0.55, 0.6), (0.6, 0.65), (0.65, 0.7), (0.7, 0.8), (0.8, 1.0)]:
    sel = [(p, y) for p, y in preds if lo <= p < hi]
    if sel: cal.append({'bucket': f'{lo:.2f}-{hi:.2f}', 'n': len(sel), 'mean_pred': round(sum(p for p, _ in sel) / len(sel), 3), 'actual': round(sum(y for _, y in sel) / len(sel), 3)})
res['calibration'] = cal
# variants
var = {}
rng = np.random.default_rng(7)
for name, rows, hl in [('base_hl180', data, 180), ('base_hl90', data, 90), ('lineup_aware_hl180', relabel(data), 180), ('lineup_aware_hl90', relabel(data), 90)]:
    mdl = b.fit(rows, '2026-10-11', hl, 3.0, 1e4)
    ti, th = mdl['ti'], mdl['th']
    c = np.zeros(len(mdl['beta'])); c[ti['vitality']] = 1; c[ti['mouz']] = -1
    sd = math.sqrt(c @ np.linalg.solve(mdl['H'], c)); d = th[ti['vitality']] - th[ti['mouz']]
    ps = 1 / (1 + np.exp(-rng.normal(d, sd, 20000)))
    top = sorted(ti, key=lambda t: -th[ti[t]])[:8]
    var[name] = {'logit_diff': round(d, 3), 'sd': round(sd, 3), 'p_map': round(1 / (1 + math.exp(-d)), 3),
                 'p_series_point': round(bo5(1 / (1 + math.exp(-d))), 3), 'p_series_integrated': round(float(np.mean([bo5(x) for x in ps])), 3),
                 'top8_strength': [(t, round(float(th[ti[t]]), 3)) for t in top]}
res['variants'] = var
maps = ['Dust2', 'Mirage', 'Inferno', 'Nuke', 'Cache', 'Anubis', 'Ancient']
mw = {}
for name, rows, lm in [('lineup_aware_lam10', relabel(data), 10.0), ('lineup_aware_lam30', relabel(data), 30.0), ('base_lam30', data, 30.0)]:
    mdl = b.fit(rows, '2026-10-11', 180, 3.0, lm)
    pm = {m: round(b.prob(mdl, 'vitality', 'mouz', m), 3) for m in maps}
    order = ['Dust2', 'Mirage', 'Inferno', 'Nuke', 'Cache']
    dist = series_dist([pm[m] for m in order])
    mw[name] = {'p_map': pm, 'assumed_order': order, 'scorelines': {k: round(v, 3) for k, v in dist.items()},
                'p_series': round(sum(v for k, v in dist.items() if k.startswith('3')), 3)}
res['map_aware'] = mw
res['vrs_implied'] = {'vitality_points': 1911, 'mouz_points': 1863, 'formula': '1/(1+10^(-(1911-1863)/400))',
                      'p_series': round(1 / (1 + 10 ** (-(1911 - 1863) / 400)), 3)}
json.dump(res, open(OUT, 'w'), indent=1)
print(json.dumps(res, indent=1)[:6000])
