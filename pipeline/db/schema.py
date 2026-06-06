# ============================================================
# Ronaldo Free Kick Analysis — DuckDB Schema
# ============================================================
# Defines all core tables.
# Run directly to initialise the database:
#   python -m pipeline.db.schema
# Or call create_all_tables() from the pipeline entry point.
# ============================================================

from pipeline.db.connection import get_connection


# ------------------------------------------------------------
# RAW SHOTS
# One row per row as received from source.
# No deduplication, no enrichment. Source of truth for raw data.
# ------------------------------------------------------------
RAW_SHOTS_DDL = """
CREATE TABLE IF NOT EXISTS raw_shots (
    -- Identity
    id                  VARCHAR PRIMARY KEY,   -- composite key: source_source_id
    source              VARCHAR NOT NULL,      -- 'understat' | 'fbref' | 'whoscored' | 'sofascore' | 'statsbomb'
    source_id           VARCHAR NOT NULL,      -- native ID from that source

    -- Player
    player_id           VARCHAR NOT NULL,      -- internal player key (see players table)
    player_name         VARCHAR NOT NULL,

    -- Match context
    match_id            VARCHAR,
    season              VARCHAR,               -- e.g. '2014/15'
    competition         VARCHAR,               -- e.g. 'La Liga'
    match_date          DATE,
    home_team           VARCHAR,
    away_team           VARCHAR,
    for_team            VARCHAR,               -- team Ronaldo was playing for

    -- Shot detail
    minute              INTEGER,
    shot_type           VARCHAR,               -- 'direct_free_kick' | 'indirect_free_kick' | 'open_play' etc
    outcome             VARCHAR,               -- 'goal' | 'saved' | 'blocked' | 'off_target' | 'post'
    x                   DOUBLE,               -- pitch x coordinate (0-100 scale)
    y                   DOUBLE,               -- pitch y coordinate (0-100 scale)
    x_end               DOUBLE,               -- shot end x (where applicable)
    y_end               DOUBLE,               -- shot end y (where applicable)

    -- xG
    xg                  DOUBLE,               -- pre-shot xG as provided by source
    xg_source           VARCHAR,              -- which model produced this xG

    -- Game state
    home_score_at_shot  INTEGER,
    away_score_at_shot  INTEGER,
    is_home             BOOLEAN,

    -- Delivery (crossed free kicks only)
    is_delivery         BOOLEAN DEFAULT FALSE,
    delivery_outcome    VARCHAR,              -- 'goal' | 'assist' | 'shot' | 'cleared' | 'incomplete'
    xa                  DOUBLE,              -- expected assists (where available)

    -- Metadata
    scraped_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    raw_json            JSON                 -- full original response stored for audit
);
"""

# ------------------------------------------------------------
# PROCESSED SHOTS
# One row per unique free kick attempt after deduplication
# and enrichment. This is the table analysis runs against.
# ------------------------------------------------------------
PROCESSED_SHOTS_DDL = """
CREATE TABLE IF NOT EXISTS processed_shots (
    -- Identity
    id                  VARCHAR PRIMARY KEY,   -- retained from raw_shots
    source              VARCHAR NOT NULL,
    source_ids          VARCHAR[],             -- all source IDs that matched to this attempt

    -- Player
    player_id           VARCHAR NOT NULL,
    player_name         VARCHAR NOT NULL,

    -- Match context
    match_id            VARCHAR,
    season              VARCHAR,
    competition         VARCHAR,
    competition_tier    VARCHAR,              -- 'domestic_top' | 'champions_league' | 'international' | 'saudi'
    match_date          DATE,
    for_team            VARCHAR,

    -- Career phase
    phase_id            INTEGER,             -- 1-6, see phases config
    phase_label         VARCHAR,             -- e.g. 'Real Madrid (early)'

    -- Shot detail
    minute              INTEGER,
    minute_bucket       VARCHAR,             -- '0-15' | '16-30' | '31-45' | '46-60' | '61-75' | '76-90' | '90+'
    outcome             VARCHAR,             -- standardised: 'goal' | 'saved' | 'blocked' | 'off_target' | 'post'
    on_target           BOOLEAN,             -- goal or saved
    is_goal             BOOLEAN,

    -- Location
    x                   DOUBLE,
    y                   DOUBLE,
    distance_m          DOUBLE,              -- calculated distance from centre of goal in metres
    angle_deg           DOUBLE,              -- calculated angle to goal in degrees
    zone_id             VARCHAR,             -- zone classification (see zones config)
    zone_label          VARCHAR,
    is_preferred_zone   BOOLEAN,             -- within Ronaldo's documented preferred range

    -- xG
    xg                  DOUBLE,
    xg_source           VARCHAR,
    xg_available        BOOLEAN,             -- FALSE for pre-2014/15 shots

    -- Game state
    scoreline_state     VARCHAR,             -- 'winning' | 'drawing' | 'losing'
    score_diff          INTEGER,             -- goals ahead (positive) or behind (negative)
    is_home             BOOLEAN,
    match_importance    VARCHAR,             -- 'knockout' | 'league' | 'group'

    -- Technique
    technique           VARCHAR,             -- 'knuckleball' | 'swerve' | 'driven' | 'unknown'
    technique_source    VARCHAR,             -- 'video_review' | 'inferred'

    -- Delivery
    is_delivery         BOOLEAN DEFAULT FALSE,
    delivery_outcome    VARCHAR,
    xa                  DOUBLE,

    -- Data quality
    has_coordinates     BOOLEAN,
    has_xg              BOOLEAN,
    data_quality_flag   VARCHAR,             -- any known issues with this record

    -- Metadata
    processed_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# ------------------------------------------------------------
# PLAYERS
# Lookup table for Ronaldo + all comparison players.
# Stores native IDs across all sources.
# ------------------------------------------------------------
PLAYERS_DDL = """
CREATE TABLE IF NOT EXISTS players (
    -- Identity
    player_id           VARCHAR PRIMARY KEY,   -- internal key e.g. 'ronaldo' | 'messi' | 'kroos'
    player_name         VARCHAR NOT NULL,
    nationality         VARCHAR,
    position            VARCHAR,

    -- Source IDs
    understat_id        VARCHAR,
    fbref_id            VARCHAR,
    whoscored_id        VARCHAR,
    sofascore_id        VARCHAR,
    transfermarkt_id    VARCHAR,
    statsbomb_id        VARCHAR,

    -- Comparison group
    comparison_group    VARCHAR[],            -- ['elite_specialist'] | ['club_teammate'] | ['league_baseline'] — can be multiple
    clubs_with_ronaldo  VARCHAR[],            -- for teammates: which clubs overlap with Ronaldo

    -- Metadata
    notes               VARCHAR              -- any data coverage notes
);
"""

# ------------------------------------------------------------
# SEASONS
# Season-level aggregates per player.
# Pre-computed and exported to seasons.json.
# ------------------------------------------------------------
SEASONS_DDL = """
CREATE TABLE IF NOT EXISTS seasons (
    -- Identity
    id                  VARCHAR PRIMARY KEY,  -- player_id + '_' + season
    player_id           VARCHAR NOT NULL,
    season              VARCHAR NOT NULL,     -- e.g. '2014/15'

    -- Club context
    club                VARCHAR,
    competition         VARCHAR,
    competition_tier    VARCHAR,
    phase_id            INTEGER,
    phase_label         VARCHAR,

    -- Volume
    direct_fk_attempts  INTEGER DEFAULT 0,
    direct_fk_goals     INTEGER DEFAULT 0,
    direct_fk_on_target INTEGER DEFAULT 0,
    direct_fk_deliveries INTEGER DEFAULT 0,

    -- Rates
    conversion_rate     DOUBLE,
    on_target_rate      DOUBLE,

    -- xG
    total_xg            DOUBLE,
    xg_per_attempt      DOUBLE,
    goals_minus_xg      DOUBLE,
    xg_available        BOOLEAN,

    -- Source
    primary_source      VARCHAR,
    data_quality_flag   VARCHAR
);
"""

# ------------------------------------------------------------
# TEAM SEASONS
# Team-level free kick data per season.
# Used for opportunity cost and team impact analysis.
# ------------------------------------------------------------
TEAM_SEASONS_DDL = """
CREATE TABLE IF NOT EXISTS team_seasons (
    -- Identity
    id                  VARCHAR PRIMARY KEY,  -- team + '_' + season
    team                VARCHAR NOT NULL,
    season              VARCHAR NOT NULL,
    competition         VARCHAR,

    -- Ronaldo context
    ronaldo_present     BOOLEAN,
    ronaldo_player_id   VARCHAR DEFAULT 'ronaldo',

    -- Team free kick volume
    team_fk_attempts    INTEGER DEFAULT 0,
    team_fk_goals       INTEGER DEFAULT 0,
    team_fk_on_target   INTEGER DEFAULT 0,

    -- Ronaldo's share
    ronaldo_fk_attempts INTEGER DEFAULT 0,
    ronaldo_fk_goals    INTEGER DEFAULT 0,
    ronaldo_share_pct   DOUBLE,              -- ronaldo_fk_attempts / team_fk_attempts

    -- xG
    team_fk_xg          DOUBLE,
    ronaldo_fk_xg       DOUBLE,
    net_xg_opportunity  DOUBLE,             -- goals_minus_xg for Ronaldo's share

    -- Source
    primary_source      VARCHAR,
    data_quality_flag   VARCHAR
);
"""

# ------------------------------------------------------------
# VIDEO LOG
# Manual technique classifications from video review.
# One row per reviewed free kick attempt.
# ------------------------------------------------------------
VIDEO_LOG_DDL = """
CREATE TABLE IF NOT EXISTS video_log (
    -- Identity
    id                  VARCHAR PRIMARY KEY,
    shot_id             VARCHAR,             -- links to processed_shots.id where matchable

    -- Match context (for unmatched records)
    match_date          DATE,
    opponent            VARCHAR,
    competition         VARCHAR,
    minute              INTEGER,
    outcome             VARCHAR,

    -- Classification
    technique           VARCHAR NOT NULL,    -- 'knuckleball' | 'swerve' | 'driven'
    run_up              VARCHAR,             -- 'long' | 'short' | 'standing'
    foot                VARCHAR,             -- 'right' | 'left'
    wall_height         VARCHAR,             -- 'high' | 'low' | 'unknown'
    keeper_position     VARCHAR,             -- 'central' | 'left' | 'right' | 'unknown'
    trajectory          VARCHAR,             -- 'dipping' | 'curling' | 'flat' | 'rising'

    -- Reviewer
    reviewer            VARCHAR DEFAULT 'manual',
    youtube_url         VARCHAR,
    reviewed_at         DATE,
    notes               VARCHAR
);
"""

# ------------------------------------------------------------
# TABLE REGISTRY
# ------------------------------------------------------------
ALL_TABLES = [
    ("raw_shots",       RAW_SHOTS_DDL),
    ("processed_shots", PROCESSED_SHOTS_DDL),
    ("players",         PLAYERS_DDL),
    ("seasons",         SEASONS_DDL),
    ("team_seasons",    TEAM_SEASONS_DDL),
    ("video_log",       VIDEO_LOG_DDL),
]


def create_all_tables(conn=None) -> None:
    """Create all tables. Idempotent — safe to run on an existing database."""
    close_after = False
    if conn is None:
        conn = get_connection()
        close_after = True

    for table_name, ddl in ALL_TABLES:
        conn.execute(ddl)
        print(f"  ✓ {table_name}")

    if close_after:
        conn.close()


def drop_all_tables(conn=None) -> None:
    """Drop all tables. Destructive — use only in development."""
    close_after = False
    if conn is None:
        conn = get_connection()
        close_after = True

    for table_name, _ in reversed(ALL_TABLES):
        conn.execute(f"DROP TABLE IF EXISTS {table_name}")
        print(f"  ✗ {table_name}")

    if close_after:
        conn.close()


if __name__ == "__main__":
    print("Initialising DuckDB schema...")
    create_all_tables()
    print("Schema initialised successfully.")