# Analysis pipeline

Everything in the main report can be regenerated from these scripts. Run them from this folder (Python 3.11+, `numpy`).
Intermediate files are written to `analysis/work/`, which is git-ignored.

| Step | Command | What it does |
|---|---|---|
| 1 | `python3 -c "import lp; open('work/Team_Vitality_Matches.html','w').write(lp.parse_html('Team_Vitality/Matches')); open('work/MOUZ_Matches.html','w').write(lp.parse_html('MOUZ/Matches'))"` | Downloads both teams' Liquipedia match-history pages (polite, cached, rate-limited API client in `lp.py`) |
| 2 | `python3 parse_matches.py work/Team_Vitality_Matches.html work/MOUZ_Matches.html` | Lists every tournament page both teams played |
| 3 | `python3 fetch_tournaments.py` | Pulls the raw wikitext of every one of those tournament pages and parses every `{{Match}}` record (map scores, half-by-half CT/T rounds, overtime, HLTV ids) via `match2.py` |
| 4 | `python3 build_logs.py` | Builds de-duplicated series logs per team (`work/log_*.json`) |
| 5 | `python3 analyze.py` | Series/map/round records, side splits, close-map, overtime and decider records |
| 6 | `python3 make_ids.py && python3 d2.py work/hltv_ids.json work/d2_parsed.json` | Fetches the HLTV match pages (via HLTV's dust2.us mirror, 2.5 s between requests) for vetoes and per-map player Rating 3.0 |
| 7 | `python3 veto_players.py 2026-07-11 --rows --permap` | Veto tendencies and round-weighted player ratings for any window |
| 8 | `python3 bt_model.py` | Rolling-origin backtest / hyperparameter search of the Bradley-Terry map model |
| 9 | `python3 model_report.py ../data/model_results.json` | Fits the final model variants and writes the probabilities |
| 10 | `python3 export.py ../data` | Writes the CSVs in `/data` |

Data licences: Liquipedia content is CC-BY-SA 3.0 (attribution: liquipedia.net contributors). Match statistics are from HLTV.org.
