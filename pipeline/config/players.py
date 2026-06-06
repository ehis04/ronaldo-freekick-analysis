# ============================================================
# Ronaldo Free Kick Analysis — Player Configuration
# ============================================================
# Source IDs for Ronaldo and all comparison players.
# IDs marked VERIFY were not confirmed during initial research
# and must be checked before the scraper phase begins.
#
# FBRef IDs: extracted from player URL slugs (confirmed via URL)
# Understat IDs: extracted from player URL slugs (confirmed via URL)
# WhoScored IDs: extracted from player URL slugs (confirmed via URL)
# Transfermarkt IDs: to be verified manually
# SofaScore IDs: to be verified manually
# ============================================================

# ------------------------------------------------------------
# RONALDO — Primary subject of all analysis
# ------------------------------------------------------------
RONALDO = {
    "player_id":         "ronaldo",
    "player_name":       "Cristiano Ronaldo",
    "nationality":       "Portugal",
    "position":          "FW",
    "understat_id":      "2371",        # confirmed
    "fbref_id":          "dea698d9",    # confirmed
    "whoscored_id":      "11006",       # confirmed
    "sofascore_id":      "18921",       # confirmed
    "transfermarkt_id":  "8198",        # confirmed
    "statsbomb_id":      None,          # StatsBomb Open does not cover Ronaldo individually
    "comparison_group":  [],
    "clubs_with_ronaldo": [],
    "notes": "Primary subject. Career spans Man Utd (2003-09), Real Madrid (2009-18), Juventus (2018-21), Man Utd (2021-22), Al-Nassr (2023+).",
}

# ------------------------------------------------------------
# GROUP 8A — ELITE FREE KICK SPECIALISTS
# Players widely recognised as elite direct free kick takers
# across the modern era. Used for top-end peer benchmarking.
# ------------------------------------------------------------
ELITE_SPECIALISTS = [
    {
        "player_id":         "messi",
        "player_name":       "Lionel Messi",
        "nationality":       "Argentina",
        "position":          "FW",
        "understat_id":      "3",           # VERIFY — Messi played La Liga (Understat covered from 2014/15)
        "fbref_id":          "d70ce98e",    # confirmed
        "whoscored_id":      "2",           # VERIFY
        "sofascore_id":      "10346",       # VERIFY
        "transfermarkt_id":  "28003",       # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["elite_specialist"],
        "clubs_with_ronaldo": [],
        "notes": "Greatest free kick taker in goals scored (62+). Benchmark for elite comparison.",
    },
    {
        "player_id":         "juninho",
        "player_name":       "Juninho Pernambucano",
        "nationality":       "Brazil",
        "position":          "MF",
        "understat_id":      None,          # Pre-Understat era (career ended 2013)
        "fbref_id":          "d51bd6c5",    # confirmed (from search URL)
        "whoscored_id":      None,          # VERIFY — limited coverage for this era
        "sofascore_id":      None,          # VERIFY
        "transfermarkt_id":  "7848",        # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["elite_specialist"],
        "clubs_with_ronaldo": [],
        "notes": "All-time record 77 direct free kick goals. Inventor of modern knuckleball technique. Pre-xG era — secondary sources only.",
    },
    {
        "player_id":         "pirlo",
        "player_name":       "Andrea Pirlo",
        "nationality":       "Italy",
        "position":          "MF",
        "understat_id":      None,          # Limited Understat coverage (played Serie A + MLS)
        "fbref_id":          "71c5f16f",    # confirmed
        "whoscored_id":      "7795",        # VERIFY
        "sofascore_id":      "2",           # VERIFY
        "transfermarkt_id":  "7198",        # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["elite_specialist"],
        "clubs_with_ronaldo": ["juventus"],
        "notes": "Elite swerve specialist. Overlaps Ronaldo at Juventus (2018-21 — Pirlo retired 2017, so no direct overlap as player; included as benchmark). Pre-xG for prime years.",
    },
    {
        "player_id":         "beckham",
        "player_name":       "David Beckham",
        "nationality":       "England",
        "position":          "MF",
        "understat_id":      None,          # Pre-Understat era (career ended 2013)
        "fbref_id":          "53539318",    # confirmed
        "whoscored_id":      None,          # VERIFY — limited historical coverage
        "sofascore_id":      None,          # VERIFY
        "transfermarkt_id":  "3574",        # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["elite_specialist"],
        "clubs_with_ronaldo": ["manchester_united"],
        "notes": "Swerve specialist. Overlaps Ronaldo at Man Utd (2003-03; Beckham left Jan 2003, minimal overlap). Historical benchmark. Pre-xG era.",
    },
    {
        "player_id":         "eriksen",
        "player_name":       "Christian Eriksen",
        "nationality":       "Denmark",
        "position":          "MF",
        "understat_id":      "604",         # VERIFY — played Premier League (Understat covered)
        "fbref_id":          "980522ec",    # confirmed
        "whoscored_id":      "76560",       # VERIFY
        "sofascore_id":      "55049",       # VERIFY
        "transfermarkt_id":  "70631",       # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["elite_specialist"],
        "clubs_with_ronaldo": [],
        "notes": "Elite direct free kick taker. Strong Understat and FBRef coverage from Tottenham era onward.",
    },
    {
        "player_id":         "kroos",
        "player_name":       "Toni Kroos",
        "nationality":       "Germany",
        "position":          "MF",
        "understat_id":      "337",         # VERIFY — played La Liga (Understat covered)
        "fbref_id":          "6ce1f46f",    # confirmed
        "whoscored_id":      "72783",       # VERIFY
        "sofascore_id":      "37937",       # VERIFY
        "transfermarkt_id":  "42783",       # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["elite_specialist"],
        "clubs_with_ronaldo": ["real_madrid"],
        "notes": "Elite delivery and direct free kick taker. Overlaps Ronaldo at Real Madrid (2014-18). Strong data coverage.",
    },
    {
        "player_id":         "calhanoglu",
        "player_name":       "Hakan Calhanoglu",
        "nationality":       "Turkey",
        "position":          "MF",
        "understat_id":      "1229",        # VERIFY — played Bundesliga and Serie A (both covered)
        "fbref_id":          "cd0fa27b",    # confirmed (from search URL)
        "whoscored_id":      "126082",      # VERIFY
        "sofascore_id":      "175647",      # VERIFY
        "transfermarkt_id":  "79452",       # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["elite_specialist"],
        "clubs_with_ronaldo": [],
        "notes": "Modern knuckleball specialist. Top free kick scorer among active players (post-Ronaldo). Good Understat coverage.",
    },
    {
        "player_id":         "neymar",
        "player_name":       "Neymar",
        "nationality":       "Brazil",
        "position":          "FW",
        "understat_id":      "2099",        # confirmed
        "fbref_id":          "69384e5d",    # confirmed (from search URL)
        "whoscored_id":      "82636",       # VERIFY
        "sofascore_id":      "14296",       # VERIFY
        "transfermarkt_id":  "68290",       # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["elite_specialist"],
        "clubs_with_ronaldo": [],
        "notes": "Strong Champions League free kick record. Covered by Understat from La Liga and Ligue 1 spells.",
    },
]

# ------------------------------------------------------------
# GROUP 8B — DESIGNATED TAKERS AT RONALDO'S CLUBS
# The player who would have taken free kicks had Ronaldo
# not been on the pitch. Used for opportunity cost analysis.
# ------------------------------------------------------------
CLUB_TEAMMATES = [
    # Man Utd (2003-2009)
    {
        "player_id":         "van_nistelrooy",
        "player_name":       "Ruud van Nistelrooy",
        "nationality":       "Netherlands",
        "position":          "FW",
        "understat_id":      None,          # Pre-Understat era
        "fbref_id":          "15cedfcc",    # VERIFY
        "whoscored_id":      None,
        "sofascore_id":      None,
        "transfermarkt_id":  "3720",        # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["club_teammate"],
        "clubs_with_ronaldo": ["manchester_united"],
        "notes": "Man Utd designated taker 2003-06. Pre-xG era. Secondary sources only.",
    },
    # Real Madrid (2009-2018)
    {
        "player_id":         "kroos",       # already defined above — dual group membership
        "player_name":       "Toni Kroos",
        "nationality":       "Germany",
        "position":          "MF",
        "understat_id":      "337",         # VERIFY
        "fbref_id":          "6ce1f46f",    # confirmed
        "whoscored_id":      "72783",       # VERIFY
        "sofascore_id":      "37937",       # VERIFY
        "transfermarkt_id":  "42783",       # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["elite_specialist", "club_teammate"],
        "clubs_with_ronaldo": ["real_madrid"],
        "notes": "Real Madrid 2014-18. Dual group — elite specialist and club teammate.",
    },
    # Juventus (2018-2021)
    {
        "player_id":         "pjanic",
        "player_name":       "Miralem Pjanic",
        "nationality":       "Bosnia",
        "position":          "MF",
        "understat_id":      "1290",        # confirmed
        "fbref_id":          "ad6df2d5",    # confirmed
        "whoscored_id":      "30226",       # confirmed (from WhoScored URL)
        "sofascore_id":      "37716",       # VERIFY
        "transfermarkt_id":  "44804",       # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["club_teammate"],
        "clubs_with_ronaldo": ["juventus"],
        "notes": "Juventus designated taker 2018-20. Overlaps Ronaldo directly. Strong data coverage.",
    },
    {
        "player_id":         "dybala",
        "player_name":       "Paulo Dybala",
        "nationality":       "Argentina",
        "position":          "FW",
        "understat_id":      "1294",        # confirmed
        "fbref_id":          "e0921a4f",    # confirmed (from search URL)
        "whoscored_id":      "155235",      # VERIFY
        "sofascore_id":      "95777",       # VERIFY
        "transfermarkt_id":  "138307",      # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["club_teammate"],
        "clubs_with_ronaldo": ["juventus"],
        "notes": "Juventus free kick taker alongside Pjanic 2018-21. Overlaps Ronaldo directly.",
    },
    # Man Utd return (2021-2022)
    {
        "player_id":         "bruno_fernandes",
        "player_name":       "Bruno Fernandes",
        "nationality":       "Portugal",
        "position":          "MF",
        "understat_id":      "1228",        # confirmed
        "fbref_id":          "507c7bdf",    # confirmed
        "whoscored_id":      "351516",      # VERIFY
        "sofascore_id":      "240086",      # VERIFY
        "transfermarkt_id":  "240306",      # VERIFY
        "statsbomb_id":      None,
        "comparison_group":  ["club_teammate"],
        "clubs_with_ronaldo": ["manchester_united"],
        "notes": "Man Utd designated taker 2021-22. Overlaps Ronaldo's return. Strong data coverage.",
    },
]

# ------------------------------------------------------------
# GROUP 8C — LEAGUE-WIDE BASELINE
# Not individually listed players — these are computed
# at query time from all direct free kick attempts in
# the leagues Ronaldo played in during the Understat era.
# This group has no player-level records here.
# ------------------------------------------------------------
LEAGUE_BASELINE_NOTE = (
    "Group 8c (league-wide baseline) is not defined as individual players. "
    "The scraper and analysis layers compute aggregate rates across all takers "
    "in the relevant league-seasons. No individual player IDs required here."
)

# ------------------------------------------------------------
# MASTER PLAYER REGISTRY
# All individual players used anywhere in the project.
# Used by the players table in DuckDB and the scrapers.
# ------------------------------------------------------------
ALL_PLAYERS = [RONALDO] + ELITE_SPECIALISTS + [
    p for p in CLUB_TEAMMATES
    if p["player_id"] not in {ep["player_id"] for ep in ELITE_SPECIALISTS}
]

# ------------------------------------------------------------
# QUICK LOOKUP HELPERS
# ------------------------------------------------------------
PLAYER_MAP = {p["player_id"]: p for p in ALL_PLAYERS}


def get_player(player_id: str) -> dict:
    """Return player config dict by internal player_id."""
    return PLAYER_MAP[player_id]


def get_all_player_ids() -> list:
    """Return list of all internal player_id strings."""
    return list(PLAYER_MAP.keys())


def get_players_by_group(group: str) -> list:
    """Return all player dicts belonging to a given comparison group."""
    return [p for p in ALL_PLAYERS if group in p.get("comparison_group", [])]