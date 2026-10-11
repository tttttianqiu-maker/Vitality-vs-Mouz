# Vitality vs MOUZ: ESL Pro League Season 24 Grand Final (Evidence-Based Preview, v2)

> **Match:** Team Vitality vs MOUZ, **Grand Final, Best-of-5, LAN**
> **Event:** ESL Pro League Season 24, Spodek Arena, Katowice, Poland (Oct 3–11, 2026, $1,000,000, 16 teams)
> **Start:** Sunday, 11 October 2026, **17:00 CEST** (15:00 UTC / 11:00 EDT)
> **Compiled:** 11 October 2026, before the match. **Version 2:** rebuilt from raw primary data. See [What changed since v1](#1-what-changed-since-v1-corrections).

---

## TL;DR: The Call

| | |
|---|---|
| **Pick** | **Team Vitality** |
| **My probability** | **Vitality ≈ 62% / MOUZ ≈ 38%** |
| **Most likely scorelines** | **3–1 Vitality (~22%)**, 3–2 Vitality (~21%), 3–0 Vitality (~17%). MOUZ: 3–2 (~16%), 3–1 (~15%), 3–0 (~9%) |
| **Backtested model** | 57–65% Vitality across model variants (central ≈ 61%) |
| **Valve VRS points** | 57% Vitality (1911 vs 1863) |
| **Market** | HLTV 66.8%; Robinhood 67¢/34¢; one bookmaker 1.42 / 2.81 (≈ 66% after margin) |

**Why Vitality (all verified in raw data):**
- **ZywOo is the biggest edge on the server.** He has a 1.41 rating over the last 3 months (53 maps) and 1.51 since mezii returned (26 maps). **Against MOUZ he's at 1.48 over 40 maps since 2025, and 1.65 in 2026.**
- **They own the head-to-head:** 14–5 in series since May 2024, 12–3 since 2025 (28–12 in maps), **3–1 in Bo5s** (3–0 since 2025).
- **They're 6–0 in 2026 Bo5 finals** (18–2 in maps) and **15–2 in overtime maps in 2026**.
- **With the full lineup they look like the best team in the world again:** 9–1 in series since Sep 17 (20–6 maps), and 5–0 on Cache in the last 3 months.

**Why it's closer than the market says:**
- MOUZ with PR (since July 21) are **18–5 in series and 40–18 in maps**. They won BLAST Bounty Season 2 and are **3–1 vs world #1 Spirit since August**.
- **All five MOUZ players rate above 1.10 at this event.** Vitality's apEX is at 0.91 (0.97 over 3 months).
- MOUZ won the last meeting 2–0 (Sept 5), and they're **15–7 on close maps** over the last 3 months (Vitality 7–6).
- My backtest shows **map win-rate tables barely predict anything** once overall team strength is known. The "MOUZ is better on Mirage, Inferno and Nuke" argument is weak evidence, in both directions.

---

## 0. How this was researched

| Source | What was used | Volume |
|---|---|---|
| **Liquipedia API** (raw `{{Match}}` records, CC-BY-SA) | Every series both teams played since May 2024, with every map score, **half-by-half CT/T rounds** and overtime | 63 tournament pages, 1,571 match records, 1,955 map results (81 teams) used in the model |
| **HLTV match pages** (via HLTV's own dust2.us mirror) | **Full veto sequences** and **per-map player Rating 3.0 / ADR / KAST / K-D** | 218 series (every Vitality/MOUZ series since June 2025, plus all head-to-heads since 2024), 0 fetch errors |
| **Valve's official VRS GitHub** ([ValveSoftware/counter-strike_regional_standings](https://github.com/ValveSoftware/counter-strike_regional_standings)) | Official standings, points and registered rosters (Jul–Oct 2026) | 4 snapshots |
| News, interviews, previews, markets | Context, quotes, odds | ~40 articles (listed in [Sources](#sources)) |

**Validation:** My self-computed 3-month map records reproduce the HLTV figures quoted by previews exactly. Examples: Vitality Dust2 11–2 (85%), Cache 6–1 (86%), Mirage 7–3 (70%), Nuke 4–4 (50%), Anubis 4–6 (40%); MOUZ Mirage 12–2 (86%), Dust2 8–4 (67%), Nuke 8–3 (73%), Inferno 6–0, Cache 3–3, Ancient 3–6.

**Evidence grades:** ✅ verified in primary data · 🟡 secondary source only · ⚠️ sources conflict.
**All datasets and code:** [`/data`](data) (CSVs of every series, map, veto, player-map line, plus model output) and [`/analysis`](analysis) (the full pipeline).

---

## 1. What changed since v1 (corrections)

The raw data exposed errors in v1, which was built from secondary articles. All of these are fixed below.

| # | v1 said | Primary data says | Evidence |
|---|---|---|---|
| 1 | MOUZ lost Mirage **9–13** to Spirit in the semi | **5–13** (Spirit 8 CT + 5 T; MOUZ 4 T + 1 CT) | ✅ HLTV match page + Liquipedia half scores |
| 2 | Spirit beat Vitality **2–0** at EWC 2026 | **2–1** (Anubis 11–13, Nuke 16–14 OT, Mirage 3–13) | ✅ Liquipedia + HLTV |
| 3 | Vitality/MOUZ "#2/#3 on the VRS" | That's **HLTV's** ranking. Official **VRS (Oct 5): Vitality #3 (1911), MOUZ #4 (1863)**. Spirit #1 (2046), Legacy #2 (1931) | ✅ Valve GitHub |
| 4 | Head-to-head: 10 meetings listed | **19 meetings since May 2024 (Vitality 14–5)**. v1 missed IEM Chengdu 2025 (×2), BLAST Open Fall 2025, BLAST Rivals Spring 2025, BLAST Open Spring 2025 groups, EPL S21 Stage 2, BLAST World Final 2024, IEM Rio 2024 and IEM Cologne 2024 | ✅ Liquipedia |
| 5 | Vitality 2025: "9 titles + 1 final loss" | 9 titles, **2** final losses (BLAST Open London 2–3 vs G2; **IEM Chengdu 0–3 vs FURIA**, missing from the Wikipedia table v1 used) | ✅ Liquipedia |
| 6 | Missing 2026 events | Added: Vitality at **BLAST Bounty Winter** (SF loss to Falcons) and **IEM Atlanta** (QF loss to NAVI); **failed to qualify for BLAST Bounty Summer** (0–2 vs Liquid online). MOUZ at **CS Asia Championships** (3rd). MOUZ at IEM Kraków was **4th** (lost the 3rd-place match to Spirit) | ✅ Liquipedia brackets |
| 7 | ZywOo has 31 HLTV MVPs | **33** (33rd at StarSeries Fall 2026) | 🟡 Escorenews / GGScore |
| 8 | "MOUZ better on Mirage" | Only if you include the event where Vitality used stand-in jL. **With the full lineup, Vitality is 7–1 on Mirage** over the last 3 months | ✅ Liquipedia |
| 9 | Cache replaced Overpass "mid-2026" | Overpass was last played at the Major (Jun 14) and Cache first appeared at BLAST Open Fall (Aug 27). A report dates the swap to Valve's **July 8** update. Overpass was Vitality's best 2026 map (**15–1**) | ✅ data / 🟡 date |

**Errors found in other previews** (so you don't get fooled):
- Strafe's preview says "Vitality removes Anubis; MOUZ removes Ancient". **It's the reverse** (see §6). Strafe also says Vitality won the last meeting 2–0. **MOUZ won it 2–0.**
- One article says Spirit beat Vitality 2–0 at EWC. It was **2–1**.

---

## 2. Match Facts

| | |
|---|---|
| Format | Bo5. 7-map pool: **Ancient, Anubis, Cache, Dust2, Inferno, Mirage, Nuke** ✅ |
| Prize | Champion **$295,000** ($125k player share + $170k club share). Runner-up **$175,000** ($50k + $125k) ✅ |
| Event format | 16-team Swiss stage (all Bo3) → 8-team single-elimination playoffs (Bo3), Bo5 grand final ✅ |
| Stakes | Both teams have **3 EPL titles**. Vitality: S16, S21, S22. MOUZ: S10 Finals, S18, S19. Today's winner is the first to 4. Vitality **declined** the S23 invite 🟡 |

---

## 3. Rosters & Lineup History

| | Vitality (coach **XTQZZZ**) | MOUZ (coach **sycrone**, assistant Xyp9x) |
|---|---|---|
| Players | **apEX** (IGL), **ZywOo** (AWP), **ropz**, **flameZ**, **mezii** | **torzsi** (AWP), **Spinx**, **xertioN** (IGL), **xelex**, **PR** |
| 2026 changes | Same five all year. **jL stood in for mezii** (paternity leave) only at **BLAST Open Fall 2026** (Aug 27–Sep 5) ✅ (VRS roster records). apEX will miss PGL Masters Bucharest (Oct 24–31) for paternity leave, with jL in 🟡. **Both are playing today** ✅ | **Jan–Apr:** Brollan (IGL), Jimpphat, Spinx, torzsi, xertioN. **Apr 18:** Brollan & Jimpphat benched; xelex promoted from MOUZ NXT; jL on loan from NAVI (PGL Astana, CS Asia). **June Major:** Brollan back because of the roster lock. **Jul 14:** PR signed from GamerLegion; first match **Jul 21** ✅ |

**Key fact:** The current MOUZ five has played **Vitality's full five zero times.** Their only meeting (Porto, Sep 5, MOUZ 2–0) came against Vitality with jL. MOUZ coach sycrone after that win: Vitality *"still have the psychological edge"*, and MOUZ need *"a few more victories"* before the rivalry feels even 🟡 (paraphrased by Players.com.ua).

---

## 4. Rankings

| Ranking | Spirit | Vitality | MOUZ | Notes |
|---|---|---|---|---|
| **HLTV** (Oct 5) | #1 (1000) | **#2 (686)** | **#3 (562)** | 🟡 |
| **Valve VRS** (Oct 5, official) | #1 (2046) | **#3 (1911)** | **#4 (1863)** | ✅ Legacy is #2 (1931) |
| VRS history | — | Jul 6: #3 (1908); Aug 3: #5 (1836); Sep 7: #5 (1841, jL roster) | Jul 6: #6 (1762, jL roster); Aug 3: #3 (1873); **Sep 7: #2 (1902)** | ✅ |
| **My model** (lineup-aware strength, logit units) | 1.005 | **1.171 (#1)** | **0.941 (#3)** | ✅ see §9. Spring-roster MOUZ was only 0.568 |

---

## 5. Path to the Final (EPL S24), with HLTV Vetoes

**Vitality: 5–0 in series, 10–3 in maps, 151–93 in rounds**

| Date | Opponent | Result | Maps | Veto (Vitality's moves in bold) |
|---|---|---|---|---|
| Oct 3 | 1win | 2–0 | Dust2 13–1, Cache 13–5 | 1win ban Nuke, **ban Ancient**, 1win pick Dust2, **pick Cache** |
| Oct 4 | NAVI | 2–1 | Anubis 13–5, **Nuke 5–13**, Mirage 13–4 | NAVI ban Dust2, **ban Ancient**, NAVI pick Anubis, **pick Nuke**, decider Mirage |
| Oct 5 | Falcons | 2–1 | **Anubis 9–13**, Dust2 13–4, Mirage 13–8 | Falcons ban Cache, **ban Ancient**, Falcons pick Anubis, **pick Dust2**, decider Mirage |
| Oct 9 (QF) | PARIVISION | 2–0 | Inferno 13–2, Dust2 13–10 | PARI ban Nuke, **ban Ancient**, PARI pick Inferno, **pick Dust2** |
| Oct 10 (SF) | Aurora | 2–1 | **Anubis 7–13**, Cache 13–7, Mirage 13–8 | Aurora ban Dust2, **ban Ancient**, Aurora pick Anubis, **pick Cache**, decider Mirage |

**MOUZ: 5–0 in series, 10–1 in maps, 139–90 in rounds**

| Date | Opponent | Result | Maps | Veto (MOUZ's moves in bold) |
|---|---|---|---|---|
| Oct 3 | M80 | 2–0 | Cache 13–9, Mirage 13–6 | M80 ban Nuke, **ban Anubis**, M80 pick Cache, **pick Mirage** |
| Oct 4 | FURIA | 2–0 | Cache 13–4, Mirage 13–7 | FURIA ban Inferno, **ban Anubis**, FURIA pick Cache, **pick Mirage** |
| Oct 5 | Spirit | 2–0 | Dust2 13–5, Mirage 13–11 | Spirit ban Inferno, **ban Anubis**, Spirit pick Dust2, **pick Mirage** |
| Oct 9 (QF) | FURIA | 2–0 | Nuke 13–11, Inferno 13–6 | FURIA ban Mirage, **ban Anubis**, FURIA pick Nuke, **pick Inferno** |
| Oct 10 (SF) | Spirit | 2–1 | Dust2 13–7, **Mirage 5–13**, Nuke 13–11 | Spirit ban Inferno, **ban Anubis**, Spirit pick Dust2, **pick Mirage**, decider Nuke |

- **All three of Vitality's dropped maps** came on the opponent's **Anubis** pick or on Nuke. MOUZ will ban Anubis today.
- MOUZ beat **Spirit, the world #1, twice** and won both FURIA series without dropping a map.

---

## 6. Map Pool & Veto (the most predictable part of this match)

### Permabans: 100% consistent
| Team | First ban, last 3 months | In head-to-heads |
|---|---|---|
| **Vitality** | **Ancient in 22 of 22 series** ✅ | Banned Ancient in **every** meeting since May 2024 ✅ |
| **MOUZ** | **Anubis in 23 of 23 series** ✅ | Banned Anubis in every meeting where it was in the pool ✅ |

→ **The remaining 5 maps are Cache, Dust2, Inferno, Mirage and Nuke.** If the series goes the distance, every one gets played. Under independent map outcomes, the order of play doesn't change who wins the series, only the scoreline.

### Pick tendencies (last 3 months, HLTV vetoes) ✅
- **Vitality's own picks:** Dust2 7, Nuke 6, Cache 4, Inferno 4, Anubis 1. Opponents pick **Anubis** against them most often (9 times).
- **MOUZ's own picks:** **Mirage 12**, Nuke 7, Inferno 4, Dust2 1. Opponents pick Ancient (9), Dust2 (8) and Cache (6) against them.
- **The Bo5 head-to-head precedent:** In all three 2025 Bo5s (EPL S21 final, Lisbon final, Dallas final), Vitality picked **Dust2 + Inferno**, MOUZ picked **Mirage + Nuke**, and **Train** was the decider. Train is out of the pool and Cache sits in its place.
- **Most likely veto:** Vitality bans Ancient, MOUZ bans Anubis. Vitality picks Dust2 (+ Inferno or Cache), MOUZ picks Mirage (+ Nuke). **Decider: Cache (most likely) or Inferno.** Which team vetoes first is not public.

### Map-by-map (records in maps; side splits are rounds won on CT / T)
| Map | Vitality, last 3 mo (all) | Vitality, last 3 mo (**full lineup**) | MOUZ, last 3 mo (= PR era) | Head-to-head since 2025 | Model P(Vitality wins map)* |
|---|---|---|---|---|---|
| **Cache** | 6–1 (CT 66% / T 60%) | **5–0** (rounds 68%) | 3–3 (CT 67% / **T 39%**) | never played | **0.58** |
| **Dust2** | 11–2 (CT 71% / T 57%) | 7–1 | 8–4 (CT 58% / T 54%) | 6–3 (**MOUZ won the last 2**) | **0.58** |
| **Mirage** | 7–3 | **7–1** | **12–2** (CT 66% / T 51%) | 5–4 | 0.55 |
| **Inferno** | 3–2 (CT 72% / T 43%) | 3–2 | **6–0** (T side 72%!) | **9–2 Vitality** | 0.55 |
| **Nuke** | 4–4 (**T 36%**) | 2–3 | 8–3 (**T 35%**) | **5–0 Vitality** | 0.54 |
| Anubis | 4–6 | 3–5 | never played (permaban) | — | banned |
| Ancient | never played (permaban) | — | 3–6 | — | banned |

\* Lineup-aware model with regularized map effects (λ=30). The 2026 full-season records point the same way: Vitality Dust2 31–6, Inferno 16–5, Nuke 16–6, Mirage 19–9; MOUZ Mirage 26–9, Inferno 18–8, Nuke 15–10, Dust2 17–18.

**Read:** Vitality is favored on **every** remaining map, most clearly on **Cache and Dust2**. MOUZ's best shots are Mirage, Inferno and Nuke, where the model gives Vitality only ~54–55% per map. That's close to a coin flip.

**Important caveat (from the backtest, §9):** Adding team-specific map effects to the model did **not** improve out-of-sample prediction (log-loss 0.6538 without map effects vs 0.6542 with). Map win-rate tables built from 6–14 maps are mostly noise, so treat the table above as flavor, not proof.

---

## 7. Players (HLTV Rating 3.0)

*My numbers are **round-weighted averages of HLTV per-map ratings**, so they can differ by a few hundredths from HLTV's own event pages.*

| Player | Last 3 months | **EPL S24** | Since Sep 17 | **vs the other team** (since 2025) |
|---|---|---|---|---|
| **ZywOo** | **1.41** (53 maps, 85.7 ADR) | **1.43** | **1.51** | **1.48** (40 maps); **1.65 in 2026** |
| ropz | 1.16 | **1.39** | 1.28 | 1.28 |
| flameZ | 1.19 | 1.36 | 1.26 | 1.13 |
| mezii | 1.10 (39 maps) | 1.17 | 1.12 | 0.96 |
| apEX | **0.97** | **0.91** | 1.00 | 0.99 |
| **Vitality average** | **1.17** | 1.25 | 1.23 | |
| **Spinx** | **1.20** (58 maps) | **1.34** | 1.22 | 1.08 |
| torzsi | 1.19 | 1.28 | 1.12 | 0.96 |
| xertioN | 1.14 (79.5 ADR) | 1.10 | 1.14 | 1.00 |
| xelex | 1.13 | 1.22 | 1.18 | 1.23 (5 maps) |
| PR | 1.06 | 1.18 | 1.08 | — (2 maps) |
| **MOUZ average** | **1.14** | 1.22 | 1.15 | |

**Per-map highlights (last 3 months):**
- ZywOo: **Cache 1.74** (7 maps), **Dust2 1.54** (13), Mirage 1.38, Inferno 1.32, Nuke 1.23.
- MOUZ on Inferno: **Spinx 1.45, PR 1.42, xelex 1.36**.
- PR on Dust2: **0.83** (12 maps).
- apEX on Nuke: 0.80.

**HLTV Top 20 of 2025** 🟡: ZywOo **#1**, ropz #3, flameZ #7, mezii #12; Spinx #10, xertioN #16, torzsi #17.

**Story of the numbers:** The team averages are nearly equal (1.17 vs 1.14). The difference is how the rating is spread:
- **Vitality = one superstar + a weak IGL frag line.** ZywOo is 0.2 above anyone on MOUZ, while apEX is the lowest-rated player in the final.
- **MOUZ = five solid players.** Nobody drops below 1.06.

Against MOUZ specifically, ZywOo has been a cheat code: 1.48 over 40 maps.

---

## 8. Form, Head-to-Head & Clutch Indicators

### 2026 season, event by event ✅
| Event (2026) | Vitality | MOUZ |
|---|---|---|
| BLAST Bounty Winter (Jan) | SF loss 1–2 vs Falcons | — |
| IEM Kraków (Feb) | 🏆 **1st** (5–0; SF **2–0 MOUZ**; F 3–1 FURIA) | 4th (SF 0–2 Vitality; 3rd-place 0–2 Spirit) |
| PGL Cluj-Napoca (Feb) | 🏆 **1st** (6–0; groups **2–0 MOUZ**; F 3–0 PARIVISION) | 3rd |
| EPL S23 (Mar) | did not attend | QF loss 1–2 vs FUT |
| BLAST Open Spring (Mar) | 🏆 **1st** (5–0; F 3–0 NAVI) | 0–2, out in groups |
| IEM Rio (Apr) | 🏆 **1st** (F 3–0 Spirit; ESL Grand Slam) | QF loss 0–2 vs Spirit → **roster overhaul** |
| BLAST Rivals Spring (May) | 🏆 **1st** (4–0; F 3–0 NAVI) | — |
| IEM Atlanta (May) | QF loss 1–2 vs NAVI | — |
| PGL Astana / CS Asia (May) | — | 3rd / 3rd (with jL) |
| IEM Cologne Major (Jun) | QF loss 1–2 vs Falcons (Stage 3: **2–1 MOUZ**) | Stage 3 exit 1–3 |
| BLAST Bounty Summer (Jul–Aug) | **failed qualifier** (0–2 vs Liquid) | 🏆 **1st** (PR debut event; F **3–1 Spirit**) |
| Esports World Cup (Aug) | QF loss 1–2 vs Spirit | QF loss 0–2 vs FUT |
| BLAST Open Fall / Porto (Aug–Sep) | SF loss **0–2 vs MOUZ** (with jL) | **2nd** (F 1–3 Spirit) |
| StarSeries Fall (Sep) | 🏆 **1st** (F 3–1 Aurora) | 5th–6th |
| **EPL S24 (Oct)** | **Final (5–0)** | **Final (5–0)** |

### Form windows ✅
| Window | Vitality | MOUZ |
|---|---|---|
| 2026 overall | 50–12 series (81%), maps 114–38, rounds 57.8% | 43–22 (66%), maps 97–60, rounds 53.7% |
| Last 3 months (Jul 11+) | 16–6, maps 35–18 | **18–5, maps 40–18** |
| Last 3 months, full Vitality lineup only | 12–4, maps 27–12 | (same as above) |
| Since mezii's return (Sep 17+) | **9–1, maps 20–6, rounds 60.7%** | 6–2 |
| vs VRS top-10, last 3 months | 8–3 (maps 19–11) | 8–4 (maps 20–13) |
| 2025 overall | 69–13 (84%) | 50–28 (64%) |

### Clutch & big-match indicators ✅
| Indicator | Vitality | MOUZ |
|---|---|---|
| **Bo5 record since 2025** | **14–2** (maps 44–15) | **2–5** (maps 9–17) |
| Bo5 record in 2026 | **6–0** (18–2) | 1–1 |
| **Overtime maps, 2026** | **15–2** | 10–4 |
| Close maps (≤3 rounds or OT), 2026 | 36–18 | 31–20 |
| Close maps, last 3 months | 7–6 | **15–7** |
| Deciding maps (map 3 of a Bo3 / map 5 of a Bo5), 2026 | 12–9 | **15–10** |
| Deciding maps, last 3 months | 5–3 | 6–3 |

### Complete head-to-head since May 2024 ✅ (vetoes in [`data/head_to_head.csv`](data/head_to_head.csv))
| Date | Event | Winner | Score | Maps (Vitality first) |
|---|---|---|---|---|
| 2026-09-05 | BLAST Open Fall (Porto) SF | **MOUZ** | 0–2 | Dust2 11–13, Mirage 7–13 *(Vitality with jL)* |
| 2026-06-13 | IEM Cologne Major, Stage 3 | **Vitality** | 2–1 | Mirage 13–9, Dust2 7–13, Inferno 13–4 *(MOUZ with Brollan)* |
| 2026-02-16 | PGL Cluj-Napoca, groups | **Vitality** | 2–0 | Dust2 13–5, Inferno 13–8 |
| 2026-02-07 | IEM Kraków SF | **Vitality** | 2–0 | Nuke 13–7, Dust2 13–6 |
| 2025-11-08 | IEM Chengdu, playoffs | **Vitality** | 2–1 | Nuke 16–13 OT, Train 11–13, Inferno 13–10 |
| 2025-11-04 | IEM Chengdu, groups | **MOUZ** | 1–2 | Train 3–13, Nuke 13–8, Inferno 19–22 OT |
| 2025-09-06 | BLAST Open Fall 2025 (London) | **Vitality** | 2–0 | Mirage 13–7, Inferno 13–8 |
| 2025-08-02 | IEM Cologne 2025 SF | **MOUZ** | 0–2 | Mirage 9–13, Train 8–13 |
| 2025-06-21 | BLAST Austin Major SF | **Vitality** | 2–1 | Mirage 13–8, Inferno 4–13, Train 13–6 |
| 2025-05-25 | **IEM Dallas 2025 Final** | **Vitality** | **3–0** | Dust2 13–11, Mirage 13–9, Inferno 13–8 |
| 2025-05-01 | BLAST Rivals Spring 2025, groups | **Vitality** | 2–1 | Mirage 9–13, Inferno 13–9, Train 13–8 |
| 2025-03-30 | **BLAST Open Lisbon 2025 Final** | **Vitality** | **3–2** | Inferno 13–0, Mirage 11–13, Dust2 11–13, Nuke 13–7, Train 13–7 |
| 2025-03-24 | BLAST Open Lisbon 2025, groups | **Vitality** | 2–0 | Mirage 13–11, Dust2 13–11 |
| 2025-03-16 | **EPL S21 Final** | **Vitality** | **3–0** | Dust2 13–9, Nuke 13–4, Inferno 13–5 |
| 2025-03-09 | EPL S21 Stage 2 | **Vitality** | 2–0 | Inferno 13–6, Dust2 13–7 |
| 2024-11-01 | BLAST World Final 2024 | **Vitality** | 2–0 | Dust2 13–6, Mirage 13–6 |
| 2024-10-11 | IEM Rio 2024 | **MOUZ** | 1–2 | Mirage 13–7, Nuke 11–13, Inferno 10–13 |
| 2024-08-13 | IEM Cologne 2024, groups | **Vitality** | 2–0 | Dust2 13–6, Vertigo 16–13 OT |
| 2024-05-12 | **EPL S19 Final** | **MOUZ** | **0–3** | Inferno 9–13, Mirage 8–13, Nuke 5–13 |

**Totals:**
- **Since May 2024:** Vitality 14–5.
- **Since 2025:** 12–3 in series, **28–12 in maps** (25–9 on maps still in the pool).
- **Bo5s:** Vitality 3–1.
- **Per map since 2025:** Inferno 9–2, Nuke 5–0, Dust2 6–3, Mirage 5–4.

---

## 9. The Model (backtested)

**What it is:** A time-decayed, ridge-regularized **Bradley–Terry model on map results**. P(A beats B on a map) = logistic(strength_A − strength_B), with optional team-by-map terms. It's fit on 1,955 map results from 81 teams across every tournament Vitality or MOUZ played since June 2025.

**How it was validated:** I ran a rolling-origin backtest. At each of 8 cut dates (Mar 1 to Oct 1, 2026), the model was refit on past data only and then predicted the next window: **886 out-of-sample maps** in total.

| Model | Log-loss (lower is better) | Accuracy |
|---|---|---|
| Coin flip | 0.6931 | 50% |
| **Team strength only** (half-life 180 d) | **0.6538** | **62.5%** |
| + team-by-map effects (λ=30) | 0.6542 | 62.1% |
| + team-by-map effects (λ=3, weakly shrunk) | 0.6650 | 61.6% |

**Calibration** (predicted vs actual map win rate, out of sample): 52% → 53%, 57% → 60%, 63% → 61%, 67% → 68%, 73% → 75%. It's well calibrated. Only the 22 maps predicted above 80% came in a bit lower (73%).

**Result for today:**
| Variant | P(Vitality wins a map) | **P(Vitality wins Bo5)**¹ |
|---|---|---|
| Base, 180-day half-life | 0.581 | **64%** |
| Base, 90-day half-life | 0.552 | 59% |
| **Lineup-aware** (MOUZ pre/post-PR and Vitality-with-jL modeled as separate teams), 180 d | 0.557 | **60%** |
| Lineup-aware, 90 d | 0.541 | 57% |
| Lineup-aware + map effects (5-map pool) | 0.54–0.58 per map | **61%** |
| Valve VRS formula: 1 / (1 + 10^(−48/400)) | — | 57% |

¹ The four team-strength variants average over the model's parameter uncertainty. The map-aware and VRS rows are point estimates.

**Scoreline distribution** (lineup-aware, map-aware, assumed order Dust2 → Mirage → Inferno → Nuke → Cache):
- **Vitality 61%:** 3–0 = 17%, 3–1 = 22%, 3–2 = 21%
- **MOUZ 39%:** 3–2 = 16%, 3–1 = 15%, 3–0 = 9%

**What the model can't see** (I lean slightly toward Vitality on these):
1. ZywOo's specific dominance against MOUZ (1.48 over 40 maps).
2. Vitality's Bo5 and overtime record (14–2 and 15–2) vs MOUZ's Bo5 record (2–5, 0–3 vs Vitality).
3. Vitality had **about 3¾ hours more rest**: their semi started at 15:45 and MOUZ's at 19:30.

**What would favor MOUZ:** Their PR-era trend is steep (spring MOUZ rated 0.57, PR-era MOUZ 0.94). If the current roster is still improving, even the lineup-aware model may underrate them.

---

## 10. Market & Expert Consensus

| Source | Vitality | MOUZ |
|---|---|---|
| HLTV match page | 66.8% | 33.2% |
| Robinhood prediction market (match day) | 67¢ | 34¢ |
| Bookmaker odds quoted by an EGW preview (bookmaker unnamed) 🟡 | 1.42 (≈66% after margin) | 2.81 |
| skin.club preview | predicts **3–2 Vitality** | |
| Strafe preview (contains factual errors, §1) | predicts **3–1 Vitality**; fans 79% Vitality | |

The market (~66%) sits above my number (~62%). The gap is the market pricing reputation and the head-to-head more heavily than MOUZ's PR-era form.

---

## 11. Quotes & Context 🟡

- **sycrone (MOUZ coach), after beating Spirit:** said fans had seen this team crumble in exactly this kind of moment about 20 times (paraphrased); xertioN *"kept calling instantly when the spawn started with a simple direction"*; *"We are at a very different place right now. It's going to be a new matchup tomorrow."*
- **sycrone after beating Vitality in Porto (Sep 5):** Vitality still hold the psychological edge, and MOUZ need a few more wins before it feels even (paraphrased).
- **torzsi:** *"This win will give us a lot of confidence… We are a new team, so I don't think it's going to be the same [as in 2025] against Vitality."* In September he called this *"the best iteration of MOUZ ever"* and described nearly burning out earlier in 2026.
- **Spinx (Oct 8):** *"I feel more confident. I think we have all the necessary pieces… I think we are ready for this."*
- **apEX (Oct 8)**, on contending for titles: *"Were we ever not?"* On his upcoming paternity leave: *"Sometimes it's hard to focus and be sure that my partner is feeling well at home."* He is under contract until the end of 2028.
- **XTQZZZ (Vitality coach, Oct 9):** *"Our T-side is for sure back."*

---

## 12. Final Verdict

### 🏆 Vitality to win: ≈ 62% (most likely 3–1, with 3–2 close behind)

**The case in five lines:**
1. Best player in the series by a mile, and historically even better against this opponent: **ZywOo 1.48 vs MOUZ**.
2. Head-to-head **14–5** since May 2024, Bo5 **3–1**, finals since 2025 **3–0**.
3. **Bo5 machine:** 14–2 since 2025, 6–0 in 2026. Overtime **15–2** in 2026.
4. **Full-lineup Vitality since Sep 17: 9–1.** Favored on every map left after the bans, especially Cache (5–0) and Dust2 (7–1).
5. A **backtested model** independently ranks Vitality #1 in the world and makes them a 57–65% favorite.

**MOUZ's path to the upset (~38%):**
1. Win their picks (Mirage 12–2, Nuke 8–3) and steal Dust2 again. They won the last two Dust2 meetings.
2. Keep the five-man balance. All five were above 1.10 this week, while apEX sits at 0.91.
3. Turn their close-map edge (**15–7** in the last 3 months) into the 3–2 coin flips.
4. Get the decider on Inferno (6–0 lately) instead of Cache (3–3).

**What would change my mind before the match:** a late roster change or illness, or a veto that hands MOUZ both Inferno and Nuke while the decider isn't Cache. Either would push this toward 55/45.

> *This is an analytical preview, not betting advice. Even at 62/38, the underdog wins roughly 2 times in 5.*

---

## Sources

**Primary data**
- Liquipedia (CC-BY-SA 3.0): [ESL Pro League Season 24](https://liquipedia.net/counterstrike/ESL/Pro_League/Season_24) · [Team Vitality matches](https://liquipedia.net/counterstrike/Team_Vitality/Matches) · [MOUZ matches](https://liquipedia.net/counterstrike/MOUZ/Matches), plus 63 tournament pages pulled through the API (full list in [`data/tournament_pages.txt`](data/tournament_pages.txt))
- HLTV match pages (vetoes, Rating 3.0; ids in [`/data`](data)): [Vitality vs MOUZ, EPL S24 GF](https://www.hltv.org/matches/2398757/vitality-vs-mouz-esl-pro-league-season-24) · [MOUZ vs Spirit SF](https://www.hltv.org/matches/2398755/mouz-vs-spirit-esl-pro-league-season-24) · [Aurora vs Vitality SF](https://www.hltv.org/matches/2398754/aurora-vs-vitality-esl-pro-league-season-24) · [MOUZ vs Vitality, BLAST Open Porto 2026](https://www.hltv.org/matches/2396950/mouz-vs-vitality-blast-open-porto-2026) · [Vitality vs MOUZ, IEM Cologne Major 2026](https://www.hltv.org/matches/2394983/vitality-vs-mouz-iem-cologne-major-2026) · [MOUZ vs Vitality, PGL Cluj-Napoca 2026](https://www.hltv.org/matches/2389967/mouz-vs-vitality-pgl-cluj-napoca-2026) · [Vitality vs MOUZ, IEM Kraków 2026](https://www.hltv.org/matches/2389664/vitality-vs-mouz-iem-krakw-2026) (pages fetched through HLTV's mirror [dust2.us](https://www.dust2.us/matches/2398757/vitality-vs-mouz))
- Valve: [counter-strike_regional_standings](https://github.com/ValveSoftware/counter-strike_regional_standings) (`live/2026/standings_global_2026_10_05.md` and earlier snapshots)

**News, interviews, previews**
- HLTV: [Vitality beat Aurora to reach EPL final](https://www.hltv.org/news/45691/vitality-beat-aurora-to-reach-epl-final) · [MOUZ beat Spirit en route to EPL final](https://www.hltv.org/news/45693/mouz-beat-spirit-en-route-to-epl-final) · [Live updates from EPL S24 grand final](https://www.hltv.org/news/45696/live-updates-from-esl-pro-league-s24-grand-final) · [Highlights from EPL S24 playoffs](https://www.hltv.org/news/45680/highlights-from-esl-pro-league-s24-playoffs) · [Spirit take down MOUZ for BLAST Open Porto title](https://www.hltv.org/news/45467/spirit-take-down-mouz-for-blast-open-porto-title) · [MOUZ announce PR signing](https://www.hltv.org/news/45132/mouz-announce-pr-signing) · [Media: jL to stand in for Vitality](https://www.hltv.org/news/45238/media-jl-to-stand-in-for-vitality) · [Top 20 players of 2025](https://www.hltv.org/news/43492/top-20-players-of-2025-final-list)
- [skin.club: sycrone explains how MOUZ beat Spirit](https://community.skin.club/en/news/sycrone-explains-how-mouz-finally-beat-spirit-in-a-decider) · [skin.club: Vitality vs MOUZ prediction](https://community.skin.club/en/news/prediction-for-vitality-vs-mouz-esl-pro-league-season-24) · [Players.com.ua: sycrone after Porto](https://players.com.ua/en/news/mouz-geared-up-for-the-grand-final-sycrone-on-team-leadership-and-winning-psychology/) · [Players.com.ua: Spinx interview](https://players.com.ua/en/news/we-are-ready-for-this-spinx-on-young-players-xertion-the-new-sticker-system-and-the-esl-pro-league-playoffs/) · [Players.com.ua: apEX interview](https://players.com.ua/en/news/i-ve-always-wanted-to-stay-at-vitality-apex-on-8-years-with-the-club-m0nesy-bc-game-and-his-career-future/) · [BLAST.tv: torzsi, "best iteration of MOUZ ever"](https://blast.tv/cs/news/torzsi-this-is-the-best-iteration-of-mouz-ever) · [Hotspawn: grand final preview](https://www.hotspawn.com/counter-strike/news/esl-pro-league-season-24-grand-final-preview) · [Hotspawn: jL stand-in](https://www.hotspawn.com/counter-strike/news/jl-vitality-stand-in) · [Strafe preview](https://www.strafe.com/news/read/vitality-vs-mouz-epl-season-24-grand-finals-preview/) · [esportnow: MOUZ win BLAST Bounty](https://esportnow.gg/cs2/news/mouz-defeat-team-spirit-to-win-blast-bounty-malta-2026-grand-final) · [GGScore: ZywOo's 33rd MVP](https://ggscore.com/en/csgo/news/81400) · [pley.gg: HLTV Top 20 of 2025](https://pley.gg/cs2/the-hltv-top-20-players-of-2025-list/) · [playnews.gg: 2026 Cache changes](https://www.playnews.gg/en/guides/counter-strike-2-the-2026-cache-guide-callouts-rework-and-changes-up-to-the-august-3-patch) · [dust2.us: Vitality decline EPL S23 invite](https://www.dust2.us/news/69624/passion-ua-claims-epl-season-23-spot-after-vitality-falcons-decline-invites)
- Markets: [Robinhood prediction market](https://robinhood.com/us/en/prediction-markets/esports/events/mouz-vs-vitality-oct-11-2026/) · [EGW betting preview](https://egamersworld.com/counterstrike/tip/EJbyzu4pEWe/vitality-vs-mouz-2ZnID4N_d)
