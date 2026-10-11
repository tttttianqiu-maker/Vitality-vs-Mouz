"""Parse Liquipedia Match2 wikitext ({{Match ...}} templates) into structured dicts."""
import re, datetime

def balanced(s, start):
    """Return end index (exclusive) of template starting at s[start:start+2]=='{{'."""
    depth = 0
    i = start
    n = len(s)
    while i < n:
        if s.startswith('{{', i):
            depth += 1; i += 2; continue
        if s.startswith('}}', i):
            depth -= 1; i += 2
            if depth == 0:
                return i
            continue
        i += 1
    return n

def split_params(body):
    """Split template body on top-level pipes."""
    parts, depth, sq, cur = [], 0, 0, []
    i = 0
    while i < len(body):
        if body.startswith('{{', i): depth += 1; cur.append('{{'); i += 2; continue
        if body.startswith('}}', i): depth -= 1; cur.append('}}'); i += 2; continue
        if body.startswith('[[', i): sq += 1; cur.append('[['); i += 2; continue
        if body.startswith(']]', i): sq -= 1; cur.append(']]'); i += 2; continue
        c = body[i]
        if c == '|' and depth == 0 and sq == 0:
            parts.append(''.join(cur)); cur = []
        else:
            cur.append(c)
        i += 1
    parts.append(''.join(cur))
    params = {}
    pos = 0
    for p in parts[1:]:
        if '=' in p:
            k, v = p.split('=', 1)
            params[k.strip()] = v.strip()
        else:
            pos += 1
            params[str(pos)] = p.strip()
    return parts[0].strip(), params

def templates(s, name_re):
    out = []
    for m in re.finditer(r'\{\{\s*(' + name_re + r')\s*[|\n}]', s):
        st = m.start()
        en = balanced(s, st)
        out.append(s[st:en])
    return out

def inner(t):
    return t[2:-2]

MONTHS = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], 1)}

def parse_date(d):
    if not d: return None
    m = re.search(r'([A-Z][a-z]+)\s+(\d{1,2}),\s*(\d{4})', d)
    if m and m.group(1) in MONTHS:
        return f"{m.group(3)}-{MONTHS[m.group(1)]:02d}-{int(m.group(2)):02d}"
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', d)
    if m: return m.group(0)
    return None

def opp_name(v):
    m = re.search(r'\{\{\s*TeamOpponent\s*\|\s*([^|}]*)', v or '')
    if m: return m.group(1).strip().lower()
    m = re.search(r'template\s*=\s*([^|}]*)', v or '')
    return m.group(1).strip().lower() if m else (v or '').strip().lower()

def toint(x):
    try: return int(str(x).strip())
    except Exception: return None

def parse_map(v):
    ts = templates(v, 'Map')
    if not ts: return None
    _, p = split_params(inner(ts[0]))
    mp = {'map': p.get('map', '').strip(), 'finished': p.get('finished', '').strip(), 'stats': p.get('stats'), 'winner': p.get('winner')}
    halves = {}
    for k in ['t1t', 't1ct', 't2t', 't2ct']:
        halves[k] = toint(p.get(k))
    mp['t1firstside'] = p.get('t1firstside')
    s1 = s2 = None
    if halves['t1t'] is not None or halves['t1ct'] is not None:
        s1 = (halves['t1t'] or 0) + (halves['t1ct'] or 0)
        s2 = (halves['t2t'] or 0) + (halves['t2ct'] or 0)
        ot1 = ot2 = 0
        n = 1
        while f'o{n}t1t' in p or f'o{n}t1ct' in p:
            ot1 += (toint(p.get(f'o{n}t1t')) or 0) + (toint(p.get(f'o{n}t1ct')) or 0)
            ot2 += (toint(p.get(f'o{n}t2t')) or 0) + (toint(p.get(f'o{n}t2ct')) or 0)
            n += 1
        mp['ot_periods'] = n - 1
        s1 += ot1; s2 += ot2
    if s1 is None and ('score1' in p or 'score2' in p):
        s1, s2 = toint(p.get('score1')), toint(p.get('score2'))
    mp.update(halves)
    mp['s1'], mp['s2'] = s1, s2
    return mp

def parse_matches(wikitext, page):
    out = []
    for t in templates(wikitext, 'Match'):
        name, p = split_params(inner(t))
        if name.strip() != 'Match':
            continue
        o1, o2 = opp_name(p.get('opponent1')), opp_name(p.get('opponent2'))
        maps = []
        k = 1
        while f'map{k}' in p:
            mp = parse_map(p[f'map{k}'])
            if mp: maps.append(mp)
            k += 1
        out.append({'page': page, 'o1': o1, 'o2': o2, 'date': parse_date(p.get('date')), 'rawdate': p.get('date'),
                    'finished': p.get('finished'), 'hltv': p.get('hltv'), 'maps': maps,
                    'bestof': p.get('bestof'), 'walkover': p.get('walkover'), 'comment': p.get('comment')})
    return out
