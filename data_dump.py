import pandas as pd
import pymongo
import json

from pymongo.mongo_client import MongoClient

client = "mongodb+srv://dhar:<Messi_10>@cluster0.ys8kius.mongodb.net/?retryWrites=true&w=majority"

DATA_FILE_PATH = (r"C:\AI-ML\dataset_collection\train.csv")
DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns of our data: {df.shape}")
    
    df.reset_index(drop=True, inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    
    print(json_record[0])
    
    client[DATABASE][COLLECTION_NAME].insert_many(json_record)