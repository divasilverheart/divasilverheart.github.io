"""
animal_shelter.py
CRUD operations for the AAC animals collection in MongoDB.
Credentials and connection settings are loaded from environment variables.

Author: Avantika Banerjee
CS-340 | CS-499 Enhancement One
"""

import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from dotenv import load_dotenv

load_dotenv()


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self):
        # Load connection settings from environment variables.
        # See .env.example for required variable names.
        USER = os.environ.get("MONGO_USER")
        PASS = os.environ.get("MONGO_PASS")
        HOST = os.environ.get("MONGO_HOST", "localhost")
        PORT = int(os.environ.get("MONGO_PORT", 27017))
        DB   = os.environ.get("MONGO_DB", "aac")
        COL  = os.environ.get("MONGO_COL", "animals")

        try:
            self.client = MongoClient(f"mongodb://{USER}:{PASS}@{HOST}:{PORT}")
            self.client.admin.command("ping")
        except (ConnectionFailure, OperationFailure) as e:
            raise ConnectionError(
                f"Could not connect to MongoDB at {HOST}:{PORT}. "
                f"Check credentials and connection settings. Details: {e}"
            )

        self.database   = self.client[DB]
        self.collection = self.database[COL]

    def _get_next_record(self):
        # Returns the next available rec_num, or 1 if none exist.
        try:
            cursor = (
                self.collection.find({"rec_num": {"$exists": True}}, {"rec_num": 1})
                .sort("rec_num", -1)
                .limit(1)
            )
            for doc in cursor:
                return int(doc.get("rec_num", 0)) + 1
            return 1
        except Exception:
            return 1

    def create(self, data):
        """Insert a document into the animals collection. Returns True on success."""
        if not data or not isinstance(data, dict):
            return False
        try:
            if "rec_num" not in data:
                data["rec_num"] = self._get_next_record()
            self.collection.insert_one(data)
            return True
        except Exception:
            return False

    def read(self, query=None):
        """Return documents matching query as a list. Returns [] on failure."""
        if query is None:
            query = {}
        if not isinstance(query, dict):
            return []
        try:
            results = list(self.collection.find(query))
            # Remove _id to avoid serialization issues in the dashboard
            for doc in results:
                doc.pop("_id", None)
            return results
        except Exception:
            return []

    def update(self, query, values):
        """Update all documents matching query. Returns count of modified documents."""
        if not isinstance(query, dict) or not isinstance(values, dict):
            return 0
        if not query or not values:
            return 0
        try:
            result = self.collection.update_many(query, values)
            return result.modified_count
        except Exception:
            return 0

    def delete(self, query):
        """Delete all documents matching query. Returns count of deleted documents."""
        if not isinstance(query, dict) or not query:
            return 0
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception:
            return 0
