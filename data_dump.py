import pandas as pd
import os,sys
import pymongo
import json
from pymongo.mongo_client import MongoClient
from schema import write_schema_yaml


#MongoDB connection URI
uri = "mongodb+srv://sourav:dhar@cluster1.ek4ptqv.mongodb.net/?retryWrites=true&w=majority"

#DATA_FILE_PATH = (r"C:\AI-ML\dataset_collection\train.csv")
DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"

if __name__=="__main__":
    
    ROOT_DIR = os.getcwd()
    DATA_FILE_PATH = os.path.join(ROOT_DIR, "data", "train.csv")
    FILE_PATH = os.path.join(ROOT_DIR, DATA_FILE_PATH)
    
    write_schema_yaml(csv_file = DATA_FILE_PATH)
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns of our data: {df.shape}")
    
    #convert the dataframe to a list of dictonaries (JSON records)
    json_records = json.loads(df.to_json(orient="records"))
    print(json_records[0])
    
    #Establish a connection to MongoDB
    client = pymongo.MongoClient(uri)
    
    #Access the desired database and collections
    db = client[DATABASE]
    collection = db[COLLECTION_NAME]
    
    #Insert the JSON records into the collection
    collection.insert_many(json_records)
    
    #Close the mongodb connection
    client.close()