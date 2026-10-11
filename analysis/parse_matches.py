import re, html, json, sys, datetime
def parse(path):
    h = open(path).read()
    rows = re.split(r"<tr class=\"table2&#95;&#95;row--body[^\"]*\">", h)[1:]
    out = []
    for r in rows:
        ts = re.search(r'data-timestamp="(\d+)"', r)
        tier = re.search(r'title="([^"]*Tier Tournaments)"', r)
        tds = re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)
        typ = re.sub('<[^>]+>', '', tds[2]).strip() if len(tds) > 2 else ''
        tour = re.search(r'<td data-nowrap=""><a href="/counterstrike/([^"#]+)(#[^"]*)?" title="([^"]+)">([^<]+)</a></td>', r)
        res = re.search(r'data-label-type="result-(\w+)"', r)
        sc = re.search(r'<span[^>]*>(\w+)</span>&#160;&#58;&#160;<span[^>]*>(\w+)</span>', r)
        opp = re.search(r'data-sort-value="([^"]*)"><div class="block-team', r)
        out.append(dict(
            ts=int(ts.group(1)) if ts else None,
            date=datetime.datetime.fromtimestamp(int(ts.group(1)), datetime.timezone.utc).strftime('%Y-%m-%d') if ts else None,
            tier=tier.group(1).replace(' Tournaments', '') if tier else None,
            type=typ,
            page=html.unescape(tour.group(1)).replace('_', ' ') if tour else None,
            anchor=tour.group(2) if tour else None,
            tournament=html.unescape(tour.group(4)) if tour else None,
            result=res.group(1) if res else None,
            score=(sc.group(1), sc.group(2)) if sc else None,
            opponent=html.unescape(opp.group(1)) if opp else None,
        ))
    return out
if __name__ == '__main__':
    for team, path in [('Vitality', sys.argv[1]), ('MOUZ', sys.argv[2])]:
        ms = parse(path)
        json.dump(ms, open(path.replace('.html', '.json'), 'w'), indent=1)
        print(team, len(ms), 'rows; latest', ms[0]['date'], 'oldest', ms[-1]['date'])
