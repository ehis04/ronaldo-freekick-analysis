# ============================================================
# Ronaldo Free Kick Analysis — Competition Configuration
# ============================================================
# Competition IDs mapped across sources, with metadata.
# Used by scrapers to target correct competitions and by
# processors to assign competition_tier to each shot.
# ============================================================

COMPETITIONS = [
    # ----------------------------------------------------------
    # ENGLISH PREMIER LEAGUE
    # ----------------------------------------------------------
    {
        "competition_id":   "epl",
        "label":            "Premier League",
        "country":          "England",
        "tier":             "domestic_top",
        "relevant_phases":  [1, 5],          # Man Utd phases
        "understat_key":    "EPL",
        "fbref_id":         "9",
        "whoscored_id":     "2",
        "sofascore_id":     "17",
        "transfermarkt_id": "GB1",
    },
    # ----------------------------------------------------------
    # LA LIGA
    # ----------------------------------------------------------
    {
        "competition_id":   "la_liga",
        "label":            "La Liga",
        "country":          "Spain",
        "tier":             "domestic_top",
        "relevant_phases":  [2, 3],           # Real Madrid phases
        "understat_key":    "La_liga",
        "fbref_id":         "12",
        "whoscored_id":     "4",
        "sofascore_id":     "8",
        "transfermarkt_id": "ES1",
    },
    # ----------------------------------------------------------
    # SERIE A
    # ----------------------------------------------------------
    {
        "competition_id":   "serie_a",
        "label":            "Serie A",
        "country":          "Italy",
        "tier":             "domestic_top",
        "relevant_phases":  [4],              # Juventus phase
        "understat_key":    "Serie_A",
        "fbref_id":         "11",
        "whoscored_id":     "5",
        "sofascore_id":     "23",
        "transfermarkt_id": "IT1",
    },
    # ----------------------------------------------------------
    # SAUDI PRO LEAGUE
    # ----------------------------------------------------------
    {
        "competition_id":   "saudi_pro_league",
        "label":            "Saudi Pro League",
        "country":          "Saudi Arabia",
        "tier":             "saudi",
        "relevant_phases":  [6],              # Al-Nassr phase
        "understat_key":    None,             # Not covered by Understat
        "fbref_id":         "70",             # VERIFY
        "whoscored_id":     "36",             # VERIFY
        "sofascore_id":     "955",            # VERIFY
        "transfermarkt_id": "SA1",
    },
    # ----------------------------------------------------------
    # UEFA CHAMPIONS LEAGUE
    # ----------------------------------------------------------
    {
        "competition_id":   "ucl",
        "label":            "UEFA Champions League",
        "country":          "Europe",
        "tier":             "champions_league",
        "relevant_phases":  [1, 2, 3, 4, 5],
        "understat_key":    None,             # Understat does not cover UCL
        "fbref_id":         "8",
        "whoscored_id":     "100",
        "sofascore_id":     "7",
        "transfermarkt_id": "CL",
    },
    # ----------------------------------------------------------
    # FA CUP
    # ----------------------------------------------------------
    {
        "competition_id":   "fa_cup",
        "label":            "FA Cup",
        "country":          "England",
        "tier":             "domestic_cup",
        "relevant_phases":  [1, 5],
        "understat_key":    None,
        "fbref_id":         "19",
        "whoscored_id":     "21",
        "sofascore_id":     "1",              # VERIFY
        "transfermarkt_id": "FAC",
    },
    # ----------------------------------------------------------
    # COPA DEL REY
    # ----------------------------------------------------------
    {
        "competition_id":   "copa_del_rey",
        "label":            "Copa del Rey",
        "country":          "Spain",
        "tier":             "domestic_cup",
        "relevant_phases":  [2, 3],
        "understat_key":    None,
        "fbref_id":         "20",
        "whoscored_id":     "22",
        "sofascore_id":     "329",            # VERIFY
        "transfermarkt_id": "CDR",
    },
    # ----------------------------------------------------------
    # COPPA ITALIA
    # ----------------------------------------------------------
    {
        "competition_id":   "coppa_italia",
        "label":            "Coppa Italia",
        "country":          "Italy",
        "tier":             "domestic_cup",
        "relevant_phases":  [4],
        "understat_key":    None,
        "fbref_id":         "14",
        "whoscored_id":     "24",
        "sofascore_id":     "57",             # VERIFY
        "transfermarkt_id": "CIT",
    },
    # ----------------------------------------------------------
    # PORTUGAL — INTERNATIONAL
    # ----------------------------------------------------------
    {
        "competition_id":   "portugal_national",
        "label":            "Portugal National Team",
        "country":          "Portugal",
        "tier":             "international",
        "relevant_phases":  [1, 2, 3, 4, 5, 6],
        "understat_key":    None,
        "fbref_id":         None,             # International via FBRef player page
        "whoscored_id":     None,
        "sofascore_id":     None,
        "transfermarkt_id": None,
    },
    # ----------------------------------------------------------
    # UEFA EUROPEAN CHAMPIONSHIP
    # ----------------------------------------------------------
    {
        "competition_id":   "euros",
        "label":            "UEFA European Championship",
        "country":          "Europe",
        "tier":             "international",
        "relevant_phases":  [1, 2, 3, 4, 5, 6],
        "understat_key":    None,
        "fbref_id":         "676",
        "whoscored_id":     None,
        "sofascore_id":     None,
        "transfermarkt_id": "EM",
    },
    # ----------------------------------------------------------
    # FIFA WORLD CUP
    # ----------------------------------------------------------
    {
        "competition_id":   "world_cup",
        "label":            "FIFA World Cup",
        "country":          "World",
        "tier":             "international",
        "relevant_phases":  [1, 2, 3, 4, 5, 6],
        "understat_key":    None,
        "fbref_id":         "1",
        "whoscored_id":     None,
        "sofascore_id":     None,
        "transfermarkt_id": "WM",
    },
]

# Competition tier priority order (for deduplication preference)
TIER_PRIORITY = [
    "champions_league",
    "domestic_top",
    "international",
    "domestic_cup",
    "saudi",
]

# Quick lookups
COMPETITION_MAP = {c["competition_id"]: c for c in COMPETITIONS}


def get_competition(competition_id: str) -> dict:
    return COMPETITION_MAP[competition_id]


def get_competitions_for_phase(phase_id: int) -> list:
    return [c for c in COMPETITIONS if phase_id in c["relevant_phases"]]