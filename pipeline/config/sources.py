# ============================================================
# Ronaldo Free Kick Analysis — Source Configuration
# ============================================================
# Per-source metadata: coverage, gaps, rate limits, scraper notes.
# Used by scrapers and by the data quality flag system.
# ============================================================

SOURCES = {
    # ----------------------------------------------------------
    # UNDERSTAT
    # ----------------------------------------------------------
    "understat": {
        "source_id":       "understat",
        "label":           "Understat",
        "url":             "https://understat.com",
        "type":            "scrape",
        "data_type":       "shot_level",
        "coverage_from":   "2014/15",
        "coverage_to":     "present",
        "leagues_covered": ["EPL", "La Liga", "Serie A", "Bundesliga", "Ligue 1", "RFPL"],
        "has_xg":          True,
        "has_coordinates": True,
        "has_free_kick_filter": True,   # shot_type == 'DirectFreekick' available
        "rate_limit_env":  "UNDERSTAT_RATE_LIMIT_SECONDS",
        "rate_limit_default": 2,
        "requires_headless": False,
        "auth_required":   False,
        "coverage_gaps": [
            "No UCL or cup competition data",
            "No Saudi Pro League",
            "No data before 2014/15",
            "No Portugal international data",
        ],
        "scraper_notes": "Data embedded as JSON in script tags. Parse with json.loads after extracting from HTML. No auth required. Respectful rate limiting essential.",
        "existing_scraper": True,   # Pre-written scraper to be repurposed from existing project
    },

    # ----------------------------------------------------------
    # FBREF
    # ----------------------------------------------------------
    "fbref": {
        "source_id":       "fbref",
        "label":           "FBRef",
        "url":             "https://fbref.com",
        "type":            "scrape",
        "data_type":       "season_aggregate",
        "coverage_from":   "2002/03",       # Some historical data further back
        "coverage_to":     "present",
        "leagues_covered": ["EPL", "La Liga", "Serie A", "Bundesliga", "Ligue 1", "UCL", "international"],
        "has_xg":          True,            # From 2017/18 onward for most leagues
        "has_coordinates": False,
        "has_free_kick_filter": True,       # Shot type filters available in shooting tables
        "rate_limit_env":  "FBREF_RATE_LIMIT_SECONDS",
        "rate_limit_default": 3,
        "requires_headless": False,
        "auth_required":   False,
        "coverage_gaps": [
            "xG only from 2017/18 onward for most leagues",
            "No shot-level coordinates",
            "Saudi Pro League very limited",
            "Pre-2003 historical data incomplete",
        ],
        "scraper_notes": "HTML tables. Use requests + BeautifulSoup. Respect 3s rate limit strictly — site blocks scrapers. Player shooting page provides aggregate free kick stats. Season logs available for match-level data. New scraper (no existing code for FBRef).",
        "existing_scraper": False,
    },

    # ----------------------------------------------------------
    # WHOSCORED
    # ----------------------------------------------------------
    "whoscored": {
        "source_id":       "whoscored",
        "label":           "WhoScored",
        "url":             "https://www.whoscored.com",
        "type":            "headless_scrape",
        "data_type":       "match_level",
        "coverage_from":   "2007/08",       # Approximate — earlier coverage patchy
        "coverage_to":     "present",
        "leagues_covered": ["EPL", "La Liga", "Serie A", "Bundesliga", "Ligue 1"],
        "has_xg":          False,
        "has_coordinates": True,            # Match incident data includes coordinates
        "has_free_kick_filter": True,
        "rate_limit_env":  "WHOSCORED_RATE_LIMIT_SECONDS",
        "rate_limit_default": 10,
        "requires_headless": True,          # Playwright required (heavy anti-bot)
        "auth_required":   False,
        "coverage_gaps": [
            "No UCL in standard scraping path",
            "No Saudi Pro League",
            "Heavy anti-bot — most fragile scraper",
            "Earlier seasons (pre-2010) may be incomplete",
            "No xG data",
        ],
        "scraper_notes": "Playwright required. Heavy anti-bot measures. Use stealth mode. Very conservative rate limiting. Primary use: pre-2014/15 shot coordinates and match-level data to fill Understat gap.",
        "existing_scraper": True,
    },

    # ----------------------------------------------------------
    # SOFASCORE
    # ----------------------------------------------------------
    "sofascore": {
        "source_id":       "sofascore",
        "label":           "SofaScore",
        "url":             "https://www.sofascore.com",
        "type":            "api",
        "data_type":       "match_level",
        "coverage_from":   "2012/13",       # Approximate
        "coverage_to":     "present",
        "leagues_covered": ["EPL", "La Liga", "Serie A", "Saudi Pro League", "UCL", "international"],
        "has_xg":          True,            # From recent seasons
        "has_coordinates": True,
        "has_free_kick_filter": True,
        "rate_limit_env":  "SOFASCORE_RATE_LIMIT_SECONDS",
        "rate_limit_default": 5,
        "requires_headless": False,
        "auth_required":   False,
        "coverage_gaps": [
            "xG reliability varies — treat as secondary",
            "API endpoints may change without notice",
            "Historical data (pre-2016) may be incomplete",
        ],
        "scraper_notes": "Primary source for Saudi Pro League (Phase 6). Unofficial API — JSON endpoints. No formal auth but rate limit carefully. Existing scraper to be repurposed.",
        "existing_scraper": True,
    },

    # ----------------------------------------------------------
    # TRANSFERMARKT
    # ----------------------------------------------------------
    "transfermarkt": {
        "source_id":       "transfermarkt",
        "label":           "Transfermarkt",
        "url":             "https://www.transfermarkt.com",
        "type":            "scrape",
        "data_type":       "career_aggregate",
        "coverage_from":   "1990s",
        "coverage_to":     "present",
        "leagues_covered": ["all"],
        "has_xg":          False,
        "has_coordinates": False,
        "has_free_kick_filter": False,      # Goals only, no shot-type filter
        "rate_limit_env":  "TRANSFERMARKT_RATE_LIMIT_SECONDS",
        "rate_limit_default": 3,
        "requires_headless": False,
        "auth_required":   False,
        "coverage_gaps": [
            "No shot-type breakdown in standard views",
            "No xG",
            "Used primarily for career timeline and club history verification",
        ],
        "scraper_notes": "HTML scraping. Requires 'User-Agent' header mimicking browser. Good for verifying career spans, clubs, and seasons. Not primary shot data source. Existing scraper to be repurposed.",
        "existing_scraper": True,
    },

    # ----------------------------------------------------------
    # STATSBOMB OPEN DATA
    # ----------------------------------------------------------
    "statsbomb": {
        "source_id":       "statsbomb",
        "label":           "StatsBomb Open Data",
        "url":             "https://github.com/statsbomb/open-data",
        "type":            "github_download",
        "data_type":       "shot_level",
        "coverage_from":   "varies",
        "coverage_to":     "varies",
        "leagues_covered": ["select_competitions"],   # Specific tournaments/seasons only
        "has_xg":          True,
        "has_coordinates": True,
        "has_free_kick_filter": True,
        "rate_limit_env":  None,            # Direct GitHub download, no rate limiting needed
        "rate_limit_default": 0,
        "requires_headless": False,
        "auth_required":   False,
        "coverage_gaps": [
            "Only specific competitions — not full career coverage",
            "Ronaldo-relevant: limited UCL seasons, some World Cup/Euros",
            "Does not cover La Liga or Premier League comprehensively",
        ],
        "scraper_notes": "Clone or download from GitHub. JSON files. Highest data quality available. Use where coverage exists to supplement/validate other sources. No existing scraper — simple file loader.",
        "existing_scraper": False,
    },

    # ----------------------------------------------------------
    # FOOTBALL-DATA.CO.UK
    # ----------------------------------------------------------
    "football_data_uk": {
        "source_id":       "football_data_uk",
        "label":           "football-data.co.uk",
        "url":             "https://www.football-data.co.uk",
        "type":            "csv_download",
        "data_type":       "match_result",
        "coverage_from":   "1993/94",
        "coverage_to":     "present",
        "leagues_covered": ["EPL", "La Liga", "Serie A", "Bundesliga", "Ligue 1"],
        "has_xg":          False,           # Match-level result data only
        "has_coordinates": False,
        "has_free_kick_filter": False,
        "rate_limit_env":  None,
        "rate_limit_default": 1,
        "requires_headless": False,
        "auth_required":   False,
        "coverage_gaps": [
            "Match results only — no shot-level data",
            "Used for team context and scoreline verification only",
        ],
        "scraper_notes": "Direct CSV download. Very simple loader. Used for supplementary match context (team results, scorelines). Existing loader to be repurposed.",
        "existing_scraper": True,
    },
}


def get_source(source_id: str) -> dict:
    return SOURCES[source_id]


def get_sources_with_free_kick_filter() -> list:
    return [s for s in SOURCES.values() if s["has_free_kick_filter"]]


def get_sources_with_xg() -> list:
    return [s for s in SOURCES.values() if s["has_xg"]]