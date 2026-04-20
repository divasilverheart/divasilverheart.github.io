"""
indexes.py
Create indexes on the animals collection for improved query performance.

Author: Avantika Banerjee
CS-340 | CS-499 Enhancement Three
"""

from animal_shelter import AnimalShelter
from pymongo import ASCENDING

def create_indexes():
    db = AnimalShelter()

    # Compound index on the fields used by the dashboard rescue type filters.
    # This prevents a full collection scan on every filter change.
    db.collection.create_index(
        [
            ("animal_type", ASCENDING),
            ("breed", ASCENDING),
            ("sex_upon_outcome", ASCENDING),
            ("age_upon_outcome_in_weeks", ASCENDING),
        ],
        name="rescue_filter_index"
    )
    print("Created index: rescue_filter_index")

    # Index on rec_num to speed up the get_next_record query in animal_shelter.py
    db.collection.create_index(
        [("rec_num", ASCENDING)],
        name="rec_num_index"
    )
    print("Created index: rec_num_index")

    print("Done.")

if __name__ == "__main__":
    create_indexes()