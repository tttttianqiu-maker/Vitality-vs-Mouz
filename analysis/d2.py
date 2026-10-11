"""Scrape dust2.us (HLTV network) match pages: veto + per-map player stats. Polite: 2.5s between requests, cached."""
import re, html, json, os, sys, time, subprocess
D = os.path.dirname(os.path.abspath(__file__)) + '/work/d2cache/'
os.makedirs(D, exist_ok=True)
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
_last = [0.0]

def fetch(mid):
    path = f'{D}{mid}.html'
    if os.path.exists(path) and os.path.getsize(path) > 5000:
        return open(path).read()
    wait = 2.5 - (time.time() - _last[0])
    if wait > 0: time.sleep(wait)
    _last[0] = time.time()
    r = subprocess.run(['curl', '-sS', '--compressed', '-A', UA, '-o', path, '-w', '%{http_code}',
                        f'https://www.dust2.us/matches/{mid}/x'], capture_output=True, text=True, timeout=60)
    if r.stdout.strip() != '200':
        print('HTTP', r.stdout, mid, file=sys.stderr)
        return None
    return open(path).read()

def txt(s): return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()

def parse(h):
    out = {}
    t = re.search(r'<title>([^<]*)', h).group(1)
    m = re.match(r'(.*?) vs\. (.*?) at (.*?) \|', html.unescape(t))
    out['team_left'], out['team_right'], out['event'] = (m.group(1), m.group(2), m.group(3)) if m else (None, None, None)
    veto = []
    for cls, b in re.findall(r'<div class="standard-box map-container ([^"]*)">(.*?)(?=<div class="standard-box map-container|</div>\s*</div>\s*<section|<section)', h, re.S):
        name = re.search(r'map-container-map-name">([^<]*)', b)
        team = re.search(r'alt="([^"]*)"', b)
        typ = re.search(r'map-container-type">([^<]*)', b)
        l = re.search(r'score-left">([^<]*)', b); r = re.search(r'score-right">([^<]*)', b)
        veto.append({'map': name.group(1).strip() if name else None, 'team': html.unescape(team.group(1)) if team else None,
                     'type': typ.group(1).strip() if typ else cls, 'left': l.group(1).strip() if l else None,
                     'right': r.group(1).strip() if r else None})
    out['veto'] = veto
    tabs = re.findall(r'data-tab-id="(\d+)"[^>]*>([^<]*)</button>', h)
    tabnames = {tid: name.strip() for tid, name in tabs}
    stats = {}
    for tid, body in re.findall(r'data-tab-content-id="(\d+)">(.*?)(?=data-tab-content-id="|<section columns|<section class|</main>)', h, re.S):
        tname = tabnames.get(tid, tid)
        teams = []
        for tb in re.findall(r'<table[^>]*>(.*?)</table>', body, re.S):
            tn = re.search(r'match-stat-team-name[^>]*>([^<]*)', tb)
            players = []
            for row in re.findall(r'<tr>\s*<td class="match-stat-player-team[^"]*">(.*?)</tr>', tb, re.S):
                nick = re.search(r'<b>([^<]*)</b>', row)
                cells = re.findall(r'<td class="(match-stat-[a-z-]+)">(.*?)</td>', row, re.S)
                c = {k: txt(v) for k, v in cells}
                kd = c.get('match-stat-kd', '')
                km = re.match(r'(\d+)\s*-\s*(\d+)', kd)
                def f(x):
                    try: return float(x.replace('%', ''))
                    except: return None
                players.append({'nick': html.unescape(nick.group(1)) if nick else None,
                                'k': int(km.group(1)) if km else None, 'd': int(km.group(2)) if km else None,
                                'adr': f(c.get('match-stat-adr', '')), 'kast': f(c.get('match-stat-kast', '')),
                                'rating': f(c.get('match-stat-rating', ''))})
            teams.append({'team': html.unescape(tn.group(1)) if tn else None, 'players': players})
        stats[tname] = teams
    out['stats'] = stats
    return out

if __name__ == '__main__':
    ids = json.load(open(sys.argv[1]))
    res = {}
    for i, mid in enumerate(ids):
        h = fetch(mid)
        if h:
            try:
                res[mid] = parse(h)
            except Exception as e:
                print('parse error', mid, e, file=sys.stderr)
        if i % 20 == 0: print(i, mid, file=sys.stderr)
    json.dump(res, open(sys.argv[2], 'w'), indent=1)
    print('done', len(res))
