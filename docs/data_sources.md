# STARTER DOCS, JUST A SCAFFOLD
# Data Sources

## Understat

**URL:** https://understat.com
**Type:** HTML scrape (JSON embedded in script tags)
**Coverage:** Big 5 leagues (EPL, La Liga, Serie A, Bundesliga, Ligue 1) from 2014/15 onward
**Data type:** Shot-level — one row per attempt with xG, coordinates, outcome, and situation

Primary source for all xG and coordinate data in Phases 3–5. Shot situation field (`DirectFreekick`) allows direct filtering without manual classification.

**Gaps:** No UCL or cup competition data. No Saudi Pro League. No data before 2014/15. No Portugal international.

---

## FBRef

**URL:** https://fbref.com
**Type:** HTML scrape (tabular data)
**Coverage:** Big 5 leagues and major competitions from 2002/03 onward. xG from 2017/18 for most leagues.
**Data type:** Season aggregates and match logs

Used for season-level free kick breakdowns, peer comparison data, and fouls won (Category 13 — free kick earning rate). Player shooting pages provide aggregate direct free kick stats. Match logs provide per-match detail.

**Gaps:** No shot-level coordinates. xG only from 2017/18. Saudi Pro League very limited.

---

## WhoScored

**URL:** https://www.whoscored.com
**Type:** Headless browser scrape (Playwright)
**Coverage:** Big 5 leagues from approximately 2007/08
**Data type:** Match incident data with coordinates

Primary gap-fill source for Phases 1–2 (pre-Understat). Provides shot coordinates and outcomes for the early Man Utd and early Real Madrid periods where Understat has no coverage. Heavy anti-bot protection — most fragile scraper in the pipeline.

**Gaps:** No xG. No UCL in standard scraping path. Earlier seasons may be incomplete.

---

## SofaScore

**URL:** https://www.sofascore.com
**Type:** Unofficial API (JSON endpoints)
**Coverage:** Most major competitions from approximately 2012/13. Saudi Pro League well covered.
**Data type:** Match-level shot data with coordinates and xG

Primary and only structured source for Phase 6 (Al-Nassr, Saudi Pro League). xG reliability is lower than Understat — treated as secondary where both sources are available.

**Gaps:** API endpoints may change without notice. Historical data pre-2016 may be incomplete. xG model not publicly documented.

---

## Transfermarkt

**URL:** https://www.transfermarkt.com
**Type:** HTML scrape
**Coverage:** Comprehensive career history from 1990s onward
**Data type:** Career records, transfer history, club stints

Used for career timeline verification, phase boundary confirmation, and player metadata. Not a primary shot data source — no shot-type breakdown available.

---

## StatsBomb Open Data

**URL:** https://github.com/statsbomb/open-data
**Type:** GitHub JSON download
**Coverage:** Select competitions only — specific UCL seasons, some World Cup and Euros editions
**Data type:** Shot-level at highest available granularity including freeze frames

Highest quality data available where coverage exists. Used to supplement and validate other sources for covered competitions. Ronaldo-relevant coverage is limited — does not cover La Liga or Premier League comprehensively.

---

## football-data.co.uk

**URL:** https://www.football-data.co.uk
**Type:** CSV download
**Coverage:** Big 5 leagues from 1993/94
**Data type:** Match results only

Supplementary source for match context — team results and scorelines used to validate game state reconstruction. Not a shot data source.

---

## Secondary Sources (Manual / Cited)

**Opta via journalism:** Pre-database era aggregate statistics cited in published sports journalism. Used for Phase 1 (2003–2009) where structured data is unavailable. All figures cited with source.

**YouTube:** Video review for technique classification. A stratified sample of attempts from each career phase was reviewed to assign knuckleball / swerve / driven classifications.