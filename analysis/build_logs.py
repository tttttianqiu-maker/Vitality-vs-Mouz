import json, os, collections
D = os.path.dirname(os.path.abspath(__file__)) + '/work/'
raw = json.load(open(D + 'all_matches_raw.json'))
ALIAS = {'vit': 'Vitality', 'vitality': 'Vitality', 'team vitality': 'Vitality', 'mouz': 'MOUZ', 'mousesports': 'MOUZ'}
def norm(o): return ALIAS.get(o, o)

def series_from(m, team):
    a, b = norm(m['o1']), norm(m['o2'])
    if team not in (a, b): return None
    flip = (b == team)
    maps = []
    for mp in m['maps']:
        if mp['finished'] in ('skip', '') or mp['s1'] is None:
            continue
        s_t, s_o = (mp['s2'], mp['s1']) if flip else (mp['s1'], mp['s2'])
        # side halves from team's perspective
        tt, tct = (mp['t2t'], mp['t2ct']) if flip else (mp['t1t'], mp['t1ct'])
        ot_, oct_ = (mp['t1t'], mp['t1ct']) if flip else (mp['t2t'], mp['t2ct'])
        fs = mp.get('t1firstside')
        if fs and flip: fs = {'ct': 't', 't': 'ct'}.get(fs, fs)
        maps.append({'map': mp['map'].replace('Dust II', 'Dust2'), 'score': s_t, 'opp_score': s_o, 'won': s_t > s_o,
                     'team_t': tt, 'team_ct': tct, 'opp_t': ot_, 'opp_ct': oct_, 'first_side': fs,
                     'ot': mp.get('ot_periods', 0), 'stats': mp.get('stats')})
    w = sum(1 for x in maps if x['won']); l = len(maps) - w
    return {'date': m['date'], 'page': m['page'], 'opponent': b if not flip else a, 'maps': maps,
            'maps_won': w, 'maps_lost': l, 'won': w > l if maps else None, 'hltv': m['hltv'],
            'walkover': m.get('walkover'), 'finished': m.get('finished'), 'bo': len(m['maps'])}

for team in ['Vitality', 'MOUZ']:
    seen = set(); log = []
    for m in raw:
        s = series_from(m, team)
        if not s or not s['date']: continue
        if s['finished'] not in ('true', True) and not s['maps']: continue
        key = (s['date'], s['opponent'], tuple((x['map'], x['score'], x['opp_score']) for x in s['maps']))
        if key in seen: continue
        seen.add(key); log.append(s)
    log.sort(key=lambda s: s['date'], reverse=True)
    json.dump(log, open(D + f'log_{team}.json', 'w'), indent=1)
    print(team, len(log), 'series', log[-1]['date'], '->', log[0]['date'])
