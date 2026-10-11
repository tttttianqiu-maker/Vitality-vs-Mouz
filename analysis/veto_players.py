import json, os, sys, collections, glob
sys.path.insert(0, os.path.dirname(__file__))
import d2
D = os.path.dirname(os.path.abspath(__file__)) + '/work/'
logs = {t: json.load(open(D + f'log_{t}.json')) for t in ['Vitality', 'MOUZ']}

def load(mid):
    p = f'{D}d2cache/{mid}.html'
    if not os.path.exists(p) or os.path.getsize(p) < 5000: return None
    try: return d2.parse(open(p).read())
    except Exception as e: return None

def veto_report(team, start, end='9999', exclude_pages=()):
    first_ban = collections.Counter(); bans = collections.Counter(); picks = collections.Counter()
    opp_picks = collections.Counter(); played = collections.Counter(); n = 0; rows = []
    for s in logs[team]:
        if not (start <= s['date'] <= end) or not s['hltv'] or s['page'] in exclude_pages: continue
        r = load(s['hltv'])
        if not r or not r['veto']: continue
        n += 1
        my_bans = [v['map'] for v in r['veto'] if v['type'] == 'BANNED' and v['team'] == team]
        my_picks = [v['map'] for v in r['veto'] if v['type'] == 'PICKED' and v['team'] == team]
        op_picks = [v['map'] for v in r['veto'] if v['type'] == 'PICKED' and v['team'] != team]
        if my_bans: first_ban[my_bans[0]] += 1
        for m in my_bans: bans[m] += 1
        for m in my_picks: picks[m] += 1
        for m in op_picks: opp_picks[m] += 1
        rows.append((s['date'], s['opponent'], 'bans:' + '/'.join(my_bans), 'picks:' + '/'.join(my_picks),
                     'opp picks:' + '/'.join(op_picks), 'left:' + '/'.join(v['map'] for v in r['veto'] if v['type'] == 'LEFTOVER')))
    return n, first_ban, bans, picks, opp_picks, rows

def player_report(team, start, end='9999', exclude_pages=()):
    agg = collections.defaultdict(lambda: dict(maps=0, rounds=0, k=0, d=0, rsum=0.0, adrsum=0.0, kastsum=0.0))
    permap = collections.defaultdict(lambda: dict(maps=0, rounds=0, rsum=0.0))
    for s in logs[team]:
        if not (start <= s['date'] <= end) or not s['hltv'] or s['page'] in exclude_pages: continue
        r = load(s['hltv'])
        if not r: continue
        mscore = {v['map']: (int(v['left']) + int(v['right'])) for v in r['veto'] if v['left'] and v['right'] and v['left'].isdigit() and v['right'].isdigit()}
        for tab, teams in r['stats'].items():
            if tab == 'All maps' or tab not in mscore: continue
            rounds = mscore[tab]
            for t in teams:
                if t['team'] != team: continue
                for p in t['players']:
                    if p['rating'] is None: continue
                    a = agg[p['nick']]
                    a['maps'] += 1; a['rounds'] += rounds; a['k'] += p['k'] or 0; a['d'] += p['d'] or 0
                    a['rsum'] += p['rating'] * rounds; a['adrsum'] += (p['adr'] or 0) * rounds; a['kastsum'] += (p['kast'] or 0) * rounds
                    pm = permap[(p['nick'], tab)]
                    pm['maps'] += 1; pm['rounds'] += rounds; pm['rsum'] += p['rating'] * rounds
    return agg, permap

if __name__ == '__main__':
    start = sys.argv[1] if len(sys.argv) > 1 else '2026-07-11'
    for team in ['Vitality', 'MOUZ']:
        excl = ('BLAST/Open/2026/Fall',) if team == 'Vitality' and '--fulllineup' in sys.argv else ()
        n, fb, bans, picks, opp, rows = veto_report(team, start, exclude_pages=excl)
        print('=' * 10, team, f'vetoes since {start}: {n} series')
        print('  first ban:', fb.most_common()); print('  all bans:', bans.most_common()); print('  own picks:', picks.most_common()); print('  opp picks vs them:', opp.most_common())
        if '--rows' in sys.argv:
            for r in rows: print('   ', *r)
        agg, permap = player_report(team, start, exclude_pages=excl)
        print('  players (round-weighted Rating 3.0):')
        for nick, a in sorted(agg.items(), key=lambda kv: -kv[1]['rsum'] / max(1, kv[1]['rounds'])):
            if a['maps'] < 3: continue
            print(f"    {nick:10s} maps={a['maps']:3d} rating={a['rsum']/a['rounds']:.3f} ADR={a['adrsum']/a['rounds']:.1f} KAST={a['kastsum']/a['rounds']:.1f}% K-D={a['k']}-{a['d']} ({a['k']-a['d']:+d})")
        if '--permap' in sys.argv:
            maps = sorted({m for (_, m) in permap})
            print('    per-map ratings:', maps)
            for nick in sorted({n for (n, _) in permap}):
                if agg[nick]['maps'] < 3: continue
                print('     ', nick.ljust(10), ' '.join(f"{m[:4]}:{permap[(nick,m)]['rsum']/permap[(nick,m)]['rounds']:.2f}({permap[(nick,m)]['maps']})" if (nick, m) in permap else f"{m[:4]}:  -  " for m in maps))
