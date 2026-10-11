"""Export cleaned datasets to CSV for the repo."""
import json, os, csv, sys
sys.path.insert(0, os.path.dirname(__file__))
import veto_players as vp
D = os.path.dirname(os.path.abspath(__file__)) + '/work/'
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
for team in ['Vitality', 'MOUZ']:
    log = json.load(open(D + f'log_{team}.json'))
    with open(f'{OUT}/series_{team.lower()}.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['date', 'tournament_page', 'opponent', 'result', 'maps_won', 'maps_lost', 'maps', 'hltv_match_id'])
        for s in log:
            if s['date'] < '2024-05-01' or not s['maps']: continue
            w.writerow([s['date'], s['page'], s['opponent'], 'W' if s['won'] else 'L', s['maps_won'], s['maps_lost'],
                        '; '.join(f"{m['map']} {m['score']}-{m['opp_score']}{' (OT)' if m['ot'] else ''}" for m in s['maps']), s['hltv']])
    with open(f'{OUT}/maps_{team.lower()}.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['date', 'tournament_page', 'opponent', 'map', 'score', 'opp_score', 'won', 'first_side', 'ct_rounds_won', 't_rounds_won', 'opp_ct_rounds_won', 'opp_t_rounds_won', 'overtime_periods', 'hltv_mapstats_id'])
        for s in log:
            if s['date'] < '2024-05-01': continue
            for m in s['maps']:
                w.writerow([s['date'], s['page'], s['opponent'], m['map'], m['score'], m['opp_score'], int(m['won']), m['first_side'],
                            m['team_ct'], m['team_t'], m['opp_ct'], m['opp_t'], m['ot'], m['stats']])
    with open(f'{OUT}/vetoes_{team.lower()}.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['date', 'opponent', 'hltv_match_id', 'step', 'team', 'action', 'map', 'score_left', 'score_right', 'left_team'])
        for s in log:
            if s['date'] < '2026-01-01' or not s['hltv']: continue
            r = vp.load(s['hltv'])
            if not r: continue
            for i, v in enumerate(r['veto'], 1):
                w.writerow([s['date'], s['opponent'], s['hltv'], i, '' if v['type'] == 'LEFTOVER' else v['team'], v['type'], v['map'], v['left'], v['right'], r['team_left']])
    with open(f'{OUT}/player_maps_{team.lower()}.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['date', 'opponent', 'hltv_match_id', 'map', 'rounds', 'player', 'kills', 'deaths', 'adr', 'kast_pct', 'rating_3_0'])
        for s in log:
            if s['date'] < '2026-01-01' or not s['hltv']: continue
            r = vp.load(s['hltv'])
            if not r: continue
            mscore = {v['map']: (int(v['left']) + int(v['right'])) for v in r['veto'] if v['left'] and v['right'] and v['left'].isdigit() and v['right'].isdigit()}
            for tab, teams in r['stats'].items():
                if tab == 'All maps' or tab not in mscore: continue
                for t in teams:
                    if t['team'] != team: continue
                    for p in t['players']:
                        w.writerow([s['date'], s['opponent'], s['hltv'], tab, mscore[tab], p['nick'], p['k'], p['d'], p['adr'], p['kast'], p['rating']])
print('exported to', OUT)
