# ============================================================
# Ronaldo Free Kick Analysis — Career Phase Configuration
# ============================================================
# 6 career phases defined by club, date range, and context.
# Phase assignment is computed in pipeline/processors/phase_tagger.py
# using match_date against these boundaries.
# ============================================================

from datetime import date

PHASES = [
    {
        "phase_id":    1,
        "label":       "Man Utd (early)",
        "club":        "manchester_united",
        "start_date":  date(2003, 8, 1),
        "end_date":    date(2009, 6, 30),
        "technique":   "swerve_power",
        "description": "Developing technique. Swerve and power approach. High volume attempts, lower conversion. Pre-xG era — secondary sources only for this phase.",
        "data_note":   "No Understat coverage. FBRef partial. WhoScored from ~2007/08. Relies on Opta-cited journalism for aggregate figures.",
        "xg_available": False,
    },
    {
        "phase_id":    2,
        "label":       "Real Madrid (early)",
        "club":        "real_madrid",
        "start_date":  date(2009, 7, 1),
        "end_date":    date(2014, 6, 30),
        "technique":   "knuckleball_transition",
        "description": "Knuckleball transition and peak athleticism. Rapid technique evolution. Shift from swerve to knuckleball begins.",
        "data_note":   "No Understat coverage (pre-2014/15). WhoScored and FBRef cover this period.",
        "xg_available": False,
    },
    {
        "phase_id":    3,
        "label":       "Real Madrid (late)",
        "club":        "real_madrid",
        "start_date":  date(2014, 7, 1),
        "end_date":    date(2018, 6, 30),
        "technique":   "knuckleball_established",
        "description": "Established knuckleball technique. Highest volume of attempts. Kroos also designated taker — opportunity cost most relevant here.",
        "data_note":   "Full Understat coverage from 2014/15. FBRef and WhoScored complete.",
        "xg_available": True,
    },
    {
        "phase_id":    4,
        "label":       "Juventus",
        "club":        "juventus",
        "start_date":  date(2018, 7, 1),
        "end_date":    date(2021, 6, 30),
        "technique":   "knuckleball_reliance",
        "description": "Post-peak athleticism. High reliance on knuckleball. Competing with Pjanic and Dybala for set piece duties.",
        "data_note":   "Full Understat coverage. FBRef and WhoScored complete.",
        "xg_available": True,
    },
    {
        "phase_id":    5,
        "label":       "Man Utd (return)",
        "club":        "manchester_united",
        "start_date":  date(2021, 8, 1),
        "end_date":    date(2022, 11, 30),
        "technique":   "knuckleball_declining",
        "description": "Declining frequency and effectiveness. Bruno Fernandes competing for set piece duties.",
        "data_note":   "Full Understat coverage. FBRef and WhoScored complete.",
        "xg_available": True,
    },
    {
        "phase_id":    6,
        "label":       "Al-Nassr",
        "club":        "al_nassr",
        "start_date":  date(2023, 1, 1),
        "end_date":    date(2099, 12, 31),  # open-ended (ongoing career)
        "technique":   "knuckleball_saudi",
        "description": "Lower competition context. Saudi Pro League. Data quality significantly reduced.",
        "data_note":   "No Understat coverage (Saudi Pro League not included). SofaScore is primary source. FBRef partial.",
        "xg_available": False,
    },
]

# Quick lookup by phase_id
PHASE_MAP = {p["phase_id"]: p for p in PHASES}


def get_phase(phase_id: int) -> dict:
    return PHASE_MAP[phase_id]


def get_phase_for_date(match_date) -> dict:
    """Return the phase dict for a given match date."""
    from datetime import date as date_type
    if isinstance(match_date, str):
        match_date = date_type.fromisoformat(match_date)
    for phase in PHASES:
        if phase["start_date"] <= match_date <= phase["end_date"]:
            return phase
    return None


def get_phase_label(phase_id: int) -> str:
    return PHASE_MAP[phase_id]["label"]