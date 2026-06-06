# ============================================================
# Ronaldo Free Kick Analysis — Zone Configuration
# ============================================================
# Pitch coordinate system: 0-100 on both axes.
# Origin (0,0) = bottom-left corner of pitch.
# Goal is at x=100, y=34 to y=66 (centre at x=100, y=50).
# Free kicks are always in the attacking half (x >= 50).
#
# Zones are defined by distance from goal and lateral position.
# Zone classification is computed in processors/zone_classifier.py.
# ============================================================

# ------------------------------------------------------------
# DISTANCE ZONES (from centre of goal, in metres)
# Based on standard pitch dimensions (105m x 68m).
# ------------------------------------------------------------
DISTANCE_ZONES = [
    {
        "zone_id":    "D1",
        "label":      "Close range",
        "min_metres": 0,
        "max_metres": 18,
        "description": "Inside or on the edge of the penalty area. High xG territory.",
    },
    {
        "zone_id":    "D2",
        "label":      "Preferred range",
        "min_metres": 18,
        "max_metres": 25,
        "description": "Ronaldo's documented preferred zone. 18-25m from goal.",
    },
    {
        "zone_id":    "D3",
        "label":      "Long range",
        "min_metres": 25,
        "max_metres": 35,
        "description": "25-35m from goal. Reduced xG. Ronaldo attempts from here more than peers.",
    },
    {
        "zone_id":    "D4",
        "label":      "Very long range",
        "min_metres": 35,
        "max_metres": 999,
        "description": "Beyond 35m. Very low xG. Rare attempts.",
    },
]

# ------------------------------------------------------------
# ANGLE ZONES (angle to goal centre, in degrees)
# 0 degrees = straight on (central). 90 degrees = side of pitch.
# ------------------------------------------------------------
ANGLE_ZONES = [
    {
        "zone_id":    "A1",
        "label":      "Central",
        "min_degrees": 0,
        "max_degrees": 15,
        "description": "Straight-on to goal. Highest scoring probability.",
    },
    {
        "zone_id":    "A2",
        "label":      "Semi-central",
        "min_degrees": 15,
        "max_degrees": 30,
        "description": "Slight angle. Still favourable.",
    },
    {
        "zone_id":    "A3",
        "label":      "Wide angle",
        "min_degrees": 30,
        "max_degrees": 999,
        "description": "Acute angle to goal. Low scoring probability.",
    },
]

# ------------------------------------------------------------
# COMPOSITE ZONES
# Combined distance + angle classification used for heatmap
# and zone-level analysis. Labels used in frontend.
# ------------------------------------------------------------
COMPOSITE_ZONES = [
    {
        "zone_id":    "Z1",
        "label":      "Central preferred",
        "distance":   "D2",
        "angle":      "A1",
        "description": "18-25m, central. Ronaldo's sweet spot. Highest attempt volume.",
        "is_ronaldo_preferred": True,
    },
    {
        "zone_id":    "Z2",
        "label":      "Central close",
        "distance":   "D1",
        "angle":      "A1",
        "description": "Within 18m, central. High xG but less common for Ronaldo.",
        "is_ronaldo_preferred": False,
    },
    {
        "zone_id":    "Z3",
        "label":      "Central long",
        "distance":   "D3",
        "angle":      "A1",
        "description": "25-35m, central. Low xG. Ronaldo attempts more than peers here.",
        "is_ronaldo_preferred": False,
    },
    {
        "zone_id":    "Z4",
        "label":      "Semi-central preferred",
        "distance":   "D2",
        "angle":      "A2",
        "description": "18-25m, slight angle. Secondary preferred zone.",
        "is_ronaldo_preferred": True,
    },
    {
        "zone_id":    "Z5",
        "label":      "Wide preferred",
        "distance":   "D2",
        "angle":      "A3",
        "description": "18-25m, wide angle. Low probability — usually delivery territory.",
        "is_ronaldo_preferred": False,
    },
    {
        "zone_id":    "Z6",
        "label":      "Other",
        "distance":   None,
        "angle":      None,
        "description": "All other zones not covered above.",
        "is_ronaldo_preferred": False,
    },
]

# Ronaldo's documented preferred zone boundaries (used for is_preferred_zone flag)
PREFERRED_ZONE = {
    "min_metres":  18,
    "max_metres":  25,
    "max_degrees": 30,
    "description": "18-25m from goal, within 30 degrees of centre. Ronaldo's established preferred taking position.",
}

# Quick lookups
DISTANCE_ZONE_MAP  = {z["zone_id"]: z for z in DISTANCE_ZONES}
ANGLE_ZONE_MAP     = {z["zone_id"]: z for z in ANGLE_ZONES}
COMPOSITE_ZONE_MAP = {z["zone_id"]: z for z in COMPOSITE_ZONES}