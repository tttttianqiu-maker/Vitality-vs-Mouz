import json, os, collections, sys
D = os.path.dirname(os.path.abspath(__file__)) + '/work/'
logs = {t: json.load(open(D + f'log_{t}.json')) for t in ['Vitality', 'MOUZ']}

def window(log, start, end='9999', exclude=None):
    return [s for s in log if start <= s['date'] <= end and s['maps'] and not (exclude and exclude(s))]

def summarize(series, label):
    W = sum(1 for s in series if s['won']); L = len(series) - W
    maps = [m for s in series for m in s['maps']]
    mw = sum(m['won'] for m in maps)
    rw = sum(m['score'] for m in maps); rl = sum(m['opp_score'] for m in maps)
    print(f"  {label}: series {W}-{L} ({100*W/max(1,len(series)):.0f}%), maps {mw}-{len(maps)-mw} ({100*mw/max(1,len(maps)):.0f}%), rounds {rw}-{rl} ({100*rw/max(1,rw+rl):.1f}%)")

def per_map(series):
    agg = collections.defaultdict(lambda: dict(w=0, l=0, rw=0, rl=0, ctw=0, ctl=0, tw=0, tl=0))
    for s in series:
        for m in s['maps']:
            a = agg[m['map']]
            a['w'] += m['won']; a['l'] += (not m['won'])
            a['rw'] += m['score']; a['rl'] += m['opp_score']
            if m['team_ct'] is not None and m['opp_t'] is not None:
                a['ctw'] += m['team_ct']; a['ctl'] += m['opp_t']
                a['tw'] += m['team_t']; a['tl'] += m['opp_ct']
    return agg

def show_maps(series, label):
    agg = per_map(series)
    print(f"  per-map ({label}):")
    for mp, a in sorted(agg.items(), key=lambda kv: -(kv[1]['w'] + kv[1]['l'])):
        n = a['w'] + a['l']
        ct = a['ctw'] / max(1, a['ctw'] + a['ctl']); t = a['tw'] / max(1, a['tw'] + a['tl'])
        print(f"    {mp:9s} {a['w']:2d}-{a['l']:<2d} ({100*a['w']/n:5.1f}%)  rounds {100*a['rw']/max(1,a['rw']+a['rl']):5.1f}%  CT {100*ct:5.1f}%  T {100*t:5.1f}%")

def close_and_ot(series, label):
    maps = [m for s in series for m in s['maps']]
    close = [m for m in maps if abs(m['score'] - m['opp_score']) <= 3 or m['ot']]
    ot = [m for m in maps if m['ot']]
    deciders = [s['maps'][-1] for s in series if (len(s['maps']) == 3 and max(s['maps_won'], s['maps_lost']) == 2) or len(s['maps']) == 5]
    print(f"  {label}: close maps (<=3 rds or OT) {sum(m['won'] for m in close)}-{len(close)-sum(m['won'] for m in close)}; "
          f"OT {sum(m['won'] for m in ot)}-{len(ot)-sum(m['won'] for m in ot)}; deciding maps {sum(m['won'] for m in deciders)}-{len(deciders)-sum(m['won'] for m in deciders)}")

if __name__ == '__main__':
    jl_vit = lambda s: s['page'] == 'BLAST/Open/2026/Fall'  # jL stood in for mezii
    for team in ['Vitality', 'MOUZ']:
        log = logs[team]
        print('=' * 20, team)
        summarize(window(log, '2026-01-01'), '2026 all')
        summarize(window(log, '2026-07-11'), 'last 3 months (Jul 11-Oct 10)')
        if team == 'MOUZ':
            summarize(window(log, '2026-07-21'), 'PR era (Jul 21+)')
            summarize(window(log, '2026-07-21', exclude=lambda s: 'Qualifier' in s['page']), 'PR era LAN only')
        else:
            summarize(window(log, '2026-07-11', exclude=jl_vit), 'last 3 months, full lineup (excl. BLAST Open Fall w/ jL)')
            summarize(window(log, '2026-09-17'), 'since mezii return (Sep 17+)')
        summarize(window(log, '2025-01-01', '2025-12-31'), '2025')
        close_and_ot(window(log, '2026-01-01'), '2026')
        close_and_ot(window(log, '2026-07-11'), 'last 3 months')
        show_maps(window(log, '2026-07-11'), 'last 3 months')
        show_maps(window(log, '2026-01-01'), '2026 all')
