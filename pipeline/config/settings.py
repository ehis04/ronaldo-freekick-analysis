# ============================================================
# Ronaldo Free Kick Analysis — Settings & Environment Config
# ============================================================
# Loads environment variables and defines output paths.
# All pipeline modules import settings rather than calling
# os.getenv() directly.
# ============================================================

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the pipeline directory
_PIPELINE_DIR = Path(__file__).parent.parent
load_dotenv(_PIPELINE_DIR / ".env")

# ------------------------------------------------------------
# ENVIRONMENT
# ------------------------------------------------------------
PIPELINE_ENV = os.getenv("PIPELINE_ENV", "dev")
assert PIPELINE_ENV in ("dev", "prod"), f"PIPELINE_ENV must be 'dev' or 'prod', got '{PIPELINE_ENV}'"

IS_DEV  = PIPELINE_ENV == "dev"
IS_PROD = PIPELINE_ENV == "prod"

# ------------------------------------------------------------
# PATHS
# ------------------------------------------------------------
_DATA_OUTPUT_BASE = Path(os.getenv("DATA_OUTPUT_PATH", "../frontend/public/data"))

# Resolve relative to pipeline directory
if not _DATA_OUTPUT_BASE.is_absolute():
    _DATA_OUTPUT_BASE = (_PIPELINE_DIR / _DATA_OUTPUT_BASE).resolve()

# The active output path switches based on environment
DATA_OUTPUT_PATH = _DATA_OUTPUT_BASE / PIPELINE_ENV

# Database path
DB_PATH = Path(os.getenv("DB_PATH", str(_PIPELINE_DIR / "db" / "ronaldo_freekicks.duckdb")))
if not DB_PATH.is_absolute():
    DB_PATH = (_PIPELINE_DIR / DB_PATH).resolve()

# Notebooks path
NOTEBOOKS_PATH = _PIPELINE_DIR / "notebooks"

# ------------------------------------------------------------
# RATE LIMITS (seconds between requests per source)
# ------------------------------------------------------------
RATE_LIMITS = {
    "fbref":           int(os.getenv("FBREF_RATE_LIMIT_SECONDS", "3")),
    "whoscored":       int(os.getenv("WHOSCORED_RATE_LIMIT_SECONDS", "10")),
    "sofascore":       int(os.getenv("SOFASCORE_RATE_LIMIT_SECONDS", "5")),
    "understat":       int(os.getenv("UNDERSTAT_RATE_LIMIT_SECONDS", "2")),
    "transfermarkt":   int(os.getenv("TRANSFERMARKT_RATE_LIMIT_SECONDS", "3")),
    "football_data_uk": 1,
    "statsbomb":        0,
}

# ------------------------------------------------------------
# LOGGING
# ------------------------------------------------------------
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# ------------------------------------------------------------
# JSON EXPORT FILES
# All 11 JSON files the pipeline writes for the frontend.
# ------------------------------------------------------------
JSON_FILES = {
    "config":        "config.json",
    "shots":         "shots.json",
    "seasons":       "seasons.json",
    "zones":         "zones.json",
    "peers":         "peers.json",
    "team_impact":   "team_impact.json",
    "context":       "context.json",
    "career_arc":    "career_arc.json",
    "delivery":      "delivery.json",
    "international": "international.json",
    "output_share":  "output_share.json",
}


def get_output_path(file_key: str) -> Path:
    """Return the full output path for a named JSON file."""
    filename = JSON_FILES[file_key]
    return DATA_OUTPUT_PATH / filename


def ensure_output_dirs() -> None:
    """Create output directories if they don't exist."""
    DATA_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# SUMMARY (for debugging)
# ------------------------------------------------------------
def print_settings() -> None:
    print(f"PIPELINE_ENV:      {PIPELINE_ENV}")
    print(f"DATA_OUTPUT_PATH:  {DATA_OUTPUT_PATH}")
    print(f"DB_PATH:           {DB_PATH}")
    print(f"LOG_LEVEL:         {LOG_LEVEL}")


if __name__ == "__main__":
    print_settings()