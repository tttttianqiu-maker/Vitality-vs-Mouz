import json, urllib.parse, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import lp, match2

D = os.path.dirname(os.path.abspath(__file__)) + '/work/'
pages = set()
for f in ['Team_Vitality_Matches.json', 'MOUZ_Matches.json']:
    for x in json.load(open(D + f)):
        if x['date'] >= '2024-05-01' and x['page'] and not x['page'].startswith('Match of LeGGends'):
            pages.add(urllib.parse.unquote(x['page']))

def base(p):
    parts = p.split('/')
    if parts[0] in ('BLAST', 'Perfect World') or p.startswith('StarLadder/StarSeries'):
        return '/'.join(parts[:4])
    if parts[0] == 'ESL':
        return '/'.join(parts[:3])
    if parts[0] in ('Intel Extreme Masters', 'PGL', 'StarLadder', 'BetBoom Dacha'):
        return '/'.join(parts[:3])
    if parts[0] in ('Esports World Cup', 'CS Asia Championships'):
        return '/'.join(parts[:2])
    return p

bases = sorted({base(p) for p in pages})
print(len(bases), 'bases')
allp = set(pages)
for b in bases:
    allp.add(b)
allp = sorted(allp)
print(len(allp), 'pages incl. subpages')
texts = lp.wikitext(allp)
json.dump(texts, open(D + 'tournament_wikitext.json', 'w'))
matches = []
for title, w in texts.items():
    if not w: continue
    matches.extend(match2.parse_matches(w, title))
json.dump(matches, open(D + 'all_matches_raw.json', 'w'), indent=0)
names = {}
for m in matches:
    for o in (m['o1'], m['o2']):
        if 'vit' in o or 'mou' in o:
            names[o] = names.get(o, 0) + 1
print('team ids:', names)
print('total match templates', len(matches))
