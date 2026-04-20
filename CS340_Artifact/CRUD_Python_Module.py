# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    def get_next_record(self):
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
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        try:
            if data is None:
                return False
            if not isinstance(data, dict):
                return False
            if "rec_num" not in data:
                data["rec_num"] = self.get_next_record()
                
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        except Exception:
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        try:
            if query is None:
                query = {}
            
            if not isinstance(query, dict):
                return []
        
            cursor = self.collection.find(query)
            results = []
        
            for doc in cursor:
                results.append(doc)
            
            return results
    
        except Exception:
            return []
        
    # Implement the U in CRUD.
    def update(self, query, values):
        try:
            if query is None:
                return 0
            if not isinstance(query, dict):
                return 0
            if values is None:
                return 0
            if not isinstance(values, dict):
                return 0

            result = self.collection.update_many(query, values)
            return len(self.read(query))

        except Exception:
            return 0
        
    # Implement the D in CRUD.
    def delete(self, query):
        try:
            if query is None:
                return 0
            if not isinstance(query, dict):
                return 0
            count = len(self.read(query))
            result = self.collection.delete_many(query)
            return count

        except Exception:
            return 0
