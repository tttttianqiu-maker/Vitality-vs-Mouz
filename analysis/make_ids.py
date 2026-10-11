"""Collect HLTV match ids (from Liquipedia records) for dust2.us scraping."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + '/work/'
ids = []
for team in ['Vitality', 'MOUZ']:
    for s in json.load(open(D + f'log_{team}.json')):
        if (s['date'] >= '2025-06-01' or s['opponent'] in ('MOUZ', 'Vitality')) and s['hltv'] and s['hltv'] not in ids:
            ids.append(s['hltv'])
json.dump(ids, open(D + 'hltv_ids.json', 'w'))
print(len(ids), 'ids')
