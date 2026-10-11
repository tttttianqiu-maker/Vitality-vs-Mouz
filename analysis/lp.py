"""Polite Liquipedia API fetcher with on-disk cache.
Respects Liquipedia API rate limits: >=2s between query requests, >=30s between parse requests."""
import json, time, urllib.request, urllib.error, urllib.parse, gzip, os, hashlib, sys

UA = "CS2MatchResearchBot/1.0 (personal match research; low volume)"
API = "https://liquipedia.net/counterstrike/api.php"
BASE = os.path.dirname(os.path.abspath(__file__)) + "/work/lpcache"
os.makedirs(BASE, exist_ok=True)
STATE = BASE + "/_last.json"

def _wait(kind):
    try:
        st = json.load(open(STATE))
    except Exception:
        st = {}
    gap = 32 if kind == "parse" else 5
    last = max(st.get("parse", 0), st.get("query", 0)) if kind == "query" else st.get("parse", 0)
    if kind == "parse":
        last = max(st.get("parse", 0), st.get("query", 0) - 29)
    now = time.time()
    if now - last < gap:
        time.sleep(gap - (now - last))
    st[kind] = time.time()
    json.dump(st, open(STATE, "w"))

def call(params, kind="query"):
    params = dict(params)
    params["format"] = "json"
    key = hashlib.sha1(json.dumps(params, sort_keys=True).encode()).hexdigest()
    path = f"{BASE}/{key}.json"
    if os.path.exists(path):
        return json.load(open(path))
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for attempt in range(6):
        _wait(kind)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
            break
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 5:
                ra = e.headers.get("Retry-After")
                delay = int(ra) if ra and ra.isdigit() else 30 * (attempt + 1)
                print(f"429; sleeping {delay}s", file=sys.stderr)
                time.sleep(delay)
                continue
            raise
    data = json.loads(raw)
    json.dump(data, open(path, "w"))
    return data

def wikitext(titles):
    """Return {title: wikitext} for up to 50 titles (follows redirects)."""
    out = {}
    for i in range(0, len(titles), 40):
        chunk = titles[i:i+40]
        d = call({"action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main",
                  "titles": "|".join(chunk), "redirects": 1}, "query")
        q = d.get("query", {})
        for p in q.get("pages", {}).values():
            if "revisions" in p:
                out[p["title"]] = p["revisions"][0]["slots"]["main"]["*"]
            else:
                out[p["title"]] = None
        # map original names through normalization/redirects
        for n in q.get("normalized", []) + q.get("redirects", []):
            if n["to"] in out and n["from"] not in out:
                out[n["from"]] = out[n["to"]]
    return out

def parse_html(page):
    d = call({"action": "parse", "page": page, "prop": "text"}, "parse")
    return d["parse"]["text"]["*"]

def prefix_pages(prefix, limit=200):
    d = call({"action": "query", "list": "allpages", "apprefix": prefix, "aplimit": limit}, "query")
    return [p["title"] for p in d["query"]["allpages"]]

if __name__ == "__main__":
    print(json.dumps(call(json.loads(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else "query"))[:3000])
