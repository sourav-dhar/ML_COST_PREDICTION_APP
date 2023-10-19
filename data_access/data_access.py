import os,sys
from src.logger import logging
import json
import pandas as pd
from dotenv import load_dotenv
import pymongo


def mongodb_client():
    ROOT_DIR = os.getcwd()
    env_file_path = os.path.join(ROOT_DIR, ".env")
    load_dotenv(dotenv_path = env_file_path)
    
    username = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    cluster_name = os.getenv("CLUSTER_LABEL")
    
    mongodb_uri = f"mongodb+srv://{username}:{password}@{cluster_name}.mongodb.net/?retryWrites=true&w=majority"
    print(mongodb_uri)
    
    client = pymongo.MongoClient(mongodb_uri)
    
    return client
    