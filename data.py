"""
data.py
Database queries and data helpers for the Grazioso Salvare dashboard.

Author: Avantika Banerjee
CS-340 | CS-499 Enhancement One
"""

import pandas as pd
from animal_shelter import AnimalShelter

# Named column constants so the map doesn't rely on positional indexes
LAT_COL   = "location_lat"
LON_COL   = "location_long"
NAME_COL  = "name"
BREED_COL = "breed"

# Query definitions for each rescue filter type
RESCUE_QUERIES = {
    "Water Rescue": {
        "animal_type": "Dog",
        "breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]},
        "sex_upon_outcome": "Intact Female",
        "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156},
    },
    "Mountain or Wilderness": {
        "animal_type": "Dog",
        "breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog",
                          "Siberian Husky", "Rottweiler"]},
        "sex_upon_outcome": "Intact Male",
        "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156},
    },
    "Disaster or Individual Tracking": {
        "animal_type": "Dog",
        "breed": {"$in": ["Doberman Pinscher", "German Shepherd", "Golden Retriever",
                          "Bloodhound", "Rottweiler"]},
        "sex_upon_outcome": "Intact Male",
        "age_upon_outcome_in_weeks": {"$gte": 20, "$lte": 300},
    },
}


def get_db():
    """Create and return a database connection."""
    return AnimalShelter()


def fetch_filtered_data(db, filter_type):
    """Query the database for the given rescue type. Returns a DataFrame."""
    query = RESCUE_QUERIES.get(filter_type, {})
    records = db.read(query)
    if not records:
        return pd.DataFrame()
    return pd.DataFrame.from_records(records)


def get_map_coordinates(df, row_index):
    """
    Return (lat, lon, breed, name) for the selected row.
    Falls back to Austin, TX coordinates if the row or columns are unavailable.
    """
    default = (30.75, -97.48, "", "")
    if df.empty or row_index >= len(df):
        return default
    try:
        row = df.iloc[row_index]
        return (
            float(row[LAT_COL]),
            float(row[LON_COL]),
            row.get(BREED_COL, ""),
            row.get(NAME_COL, ""),
        )
    except (KeyError, ValueError, TypeError):
        return default
