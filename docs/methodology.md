# STARTER DOCS, JUST A SCAFFOLD
# Methodology

## Research Question

Was Cristiano Ronaldo a good free kick taker, and was his insistence on taking free kicks beneficial or detrimental to his teams?

---

## What Counts as a Direct Free Kick

This analysis covers **direct free kicks only** — attempts where Ronaldo shot directly at goal from a dead ball situation. Excluded:

- Indirect free kicks (passes from the spot)
- Corners
- Penalties
- Free kicks crossed or delivered into the box (tracked separately as deliveries)

---

## Data Sources and Priority

Where a shot appears in multiple sources, the following priority order is applied during deduplication:

1. **Understat** — shot-level xG and coordinates, most reliable for Big 5 leagues from 2014/15
2. **StatsBomb Open Data** — highest granularity where available
3. **FBRef** — season aggregates and match logs
4. **WhoScored** — pre-2014/15 gap fill and coordinates
5. **SofaScore** — Saudi Pro League only

---

## xG Availability

Expected goals (xG) data is only available from the **2014/15 season onward** via Understat. This covers Phases 3, 4, and 5 of Ronaldo's career.

For Phases 1 and 2 (2003–2014), analysis is limited to:
- Attempt volume
- Outcome classification (goal / saved / blocked / off target / post)
- Conversion rate
- On-target rate

All charts and tables clearly flag when xG data is unavailable for a given period.

---

## Zone Classification

Pitch coordinates use a 0–100 scale on both axes. Distance from goal and angle to goal are calculated geometrically from shot coordinates against a standard goal position.

**Ronaldo's preferred zone** is defined as 18–25m from goal within 30 degrees of centre — derived from published analysis of his documented taking positions.

Zone boundaries:

| Zone | Distance | Angle |
|---|---|---|
| Central preferred | 18–25m | 0–15° |
| Central close | 0–18m | 0–15° |
| Central long | 25–35m | 0–15° |
| Semi-central preferred | 18–25m | 15–30° |
| Wide preferred | 18–25m | 30°+ |

---

## Career Phase Definitions

Phases are assigned by match date against fixed date boundaries. Where a player moved clubs mid-season, the phase boundary follows the transfer date, not the season start.

---

## Peer Comparison Groups

**Group 8a — Elite specialists:** Players widely recognised as among the best direct free kick takers of the modern era. Selected on the basis of published goal tallies, reputation, and data availability.

**Group 8b — Club-designated takers:** The player who would have taken free kicks had Ronaldo not been present. Identified from match footage review, press reporting, and set piece statistics from each club season.

**Group 8c — League-wide baseline:** All players with 10 or more direct free kick attempts in the relevant league-seasons. Computed at query time from Understat and FBRef. No individual player records.

---

## Opportunity Cost Calculation

Net xG opportunity cost is calculated as:

```
net_xg = league_avg_xg_per_attempt × ronaldo_attempts - ronaldo_actual_xg
```

A positive value means Ronaldo's attempts produced less xG than the league average taker would have generated from the same positions. This is then compared against Ronaldo's actual goals to produce a full picture.

---

## Saudi Pro League Caveats

Phase 6 (Al-Nassr, 2023–) data quality is materially lower than the rest of the career:

- No Understat coverage
- SofaScore is the primary source — xG reliability is reduced
- Competition level is not comparable to the Big 5 leagues
- All Phase 6 figures are presented with a data quality flag

---

## Pre-2009 Caveats

Phase 1 (Man Utd early, 2003–2009) relies on secondary sources — Opta-cited journalism and FBRef historical aggregates. Shot-level data is not available. Figures for this period should be treated as estimates.

---

## Technique Classification

Technique labels (knuckleball / swerve / driven) are assigned from video review where footage is available, with phase-level inference applied where it is not. Video review covered a stratified sample of attempts from each phase. The `technique_source` field on each shot record distinguishes confirmed video classifications from inferred ones.