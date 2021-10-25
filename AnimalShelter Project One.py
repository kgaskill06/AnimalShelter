from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps, loads
import json


class AnimalShelter(object):
    """CRUD Operations for MongoDB Animal Collection"""
    def __init__(self, username, password):
        #Initializing MongoClient
        # to access MongoDB Database and collections.
        #username = "aacuser"
        #password = "admin"
        success = "Successfully Loaded"
        
        self.client = MongoClient('mongodb://%s:%s@localhost:44701/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']
        print(success)
        
    # CRUD Methods C create 
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data) #data should be a dictionary
            
            print(insert)
            return True
        
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        
    #r definition method
    def read(self, search):
    
        if search is not None:
            search_result = list(self.database.animals.find(search))#, {"_id": False}))
            #print(search_result)
            return search_result
            
        
        else:
            raise Exception("Nothing to find, because data parameter is empty")
            return False

    # def update
    def update(self, query_data, updated_data):
        """update with two parameters, data being searched for to update, and the new data"""
        
        if query_data is not None and updated_data is not None:
            update_var = self.database.animals.update_one(query_data, {'$set': updated_data}) 
            json_output = self.database.animals.find(updated_data)
            return dumps(list(json_output)) 
            
            
        else:
            raise Exception("Document failed to update")
            
            
        #json_output = list(self.database.animals.find(update_var))
        #cursor = self.database.animals.findOne(updated_data)
        
        #list_cur = list(cursor)
        #json_output = dumps(list_cur)
        #return json_output
        """updated_data  pulled from parameter and fed into update_one keeps initialzing as blank and does not return info"""
        
        json_output = self.database.animals.find(update_var)
        return dumps(list(json_output))     
                
     
    # def Delete
    def delete(self, document):
        """Delete document fed from parameter"""
        
        if document is not None:
            delete_document = self.database.animals.delete_one(document)
            json_output = self.database.animals.find(document)
            print("Delete Complete")
            return dumps(list(json_output))
            
        else:
            raise Exception("Document failed to delete")
            
