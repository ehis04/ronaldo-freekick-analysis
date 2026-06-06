# STARTER DOCS, JUST A SCAFFOLD
# Ronaldo Free Kick Analysis

A comprehensive public data analysis project investigating whether Cristiano Ronaldo's taking of direct free kicks was net beneficial or detrimental to his teams.

The finished product is a publicly deployed web application presenting the full findings interactively, free to access on desktop and mobile.

**Live site:** [ronaldo-freekicks.vercel.app](https://ronaldo-freekicks.vercel.app)

---

## Research Question

Was Cristiano Ronaldo a good free kick taker, and was his insistence on taking free kicks beneficial or detrimental to his teams?

This goes beyond conversion percentage. The analysis examines accuracy, shot quality (xG), position, opportunity cost, peer comparison across three groups, team impact, and career arc across six defined phases.

---

## Repository Structure

```
ronaldo-freekicks/
├── pipeline/          # Python data pipeline
│   ├── config/        # Player IDs, phases, zones, competitions, sources, settings
│   ├── scrapers/      # One module per data source
│   ├── processors/    # Cleaning, enrichment, transformation
│   ├── analysis/      # Computed metrics
│   ├── exporters/     # JSON file generation for the frontend
│   ├── tests/         # Progressive test suite
│   ├── notebooks/     # Exploratory analysis and methodology validation
│   ├── db/            # DuckDB schema, connection, query helpers
│   └── run_pipeline.py
├── frontend/          # React + Vite web application
│   ├── public/data/
│   │   ├── dev/       # Sample dataset — committed to repo
│   │   └── prod/      # Full pipeline output — gitignored
│   └── src/
│       ├── pages/
│       ├── components/
│       ├── hooks/
│       └── utils/
├── .github/workflows/ # Pipeline and deploy GitHub Actions
└── docs/              # Methodology, data sources, findings
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Pipeline language | Python 3.11 |
| Pipeline database | DuckDB |
| Pipeline execution | GitHub Actions |
| Frontend framework | React + Vite + TypeScript |
| Styling | Tailwind CSS + shadcn/ui |
| Charts | Recharts + D3.js |
| Tables | TanStack Table |
| Hosting | Vercel |

---

## Data Sources

| Source | Coverage | xG |
|---|---|---|
| Understat | Big 5 leagues, 2014/15–present, shot-level | Yes |
| FBRef | Season aggregates, all competitions, 2002/03–present | Partial |
| WhoScored | Match-level, 2007/08–present | No |
| SofaScore | Saudi Pro League, recent seasons | Yes |
| Transfermarkt | Career records, historical | No |
| StatsBomb Open | Select competitions, highest granularity | Yes |
| football-data.co.uk | Match results, supplementary | No |

**Key coverage gaps:** No xG available pre-2014/15. Limited structured data for the Saudi Pro League. Pre-2009 Man Utd career relies on secondary sources.

---

## Running the Pipeline Locally

```bash
cd pipeline
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env

cd ..
python pipeline/run_pipeline.py
```

The pipeline writes JSON files to `frontend/public/data/dev/` by default. Set `PIPELINE_ENV=prod` to write to `prod/`.

---

## Running the Frontend Locally

```bash
cd frontend
npm install
npm run dev
```

Opens on `http://localhost:5173`. Uses the dev sample dataset by default.

---

## Career Phases

| Phase | Period | Club | Context |
|---|---|---|---|
| 1 | 2003–2009 | Manchester United | Swerve/power, developing technique |
| 2 | 2009–2014 | Real Madrid | Knuckleball transition |
| 3 | 2014–2018 | Real Madrid | Established knuckleball, high volume |
| 4 | 2018–2021 | Juventus | Post-peak, knuckleball reliance |
| 5 | 2021–2022 | Manchester United | Declining frequency |
| 6 | 2023– | Al-Nassr | Lower competition context |

---

## Licence

Analysis, findings, and data: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
Source code: All Rights Reserved

© 2026. You may share this work with attribution but may not adapt, sell, or build upon it without permission.