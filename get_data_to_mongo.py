import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo


from dotenv import load_dotenv

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

certifi.where()
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def csv_to_json(self, filepath):
        try:
            # read the csv file in Network_Data folder
            df = pd.read_csv(filepath)
            df = df.reset_index(drop=True)
            # convert dataframe to json
            json_records = list(json.loads(df.T.to_json()).values())
            return json_records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def push_to_mongo(self, records: list, database_name: str, collection_name: str) -> int:
        """
        Inserts records into a MongoDB collection.

        Args:
            records (list): A list of dictionaries to insert into the collection.
            database_name (str): The name of the MongoDB database.
            collection_name (str): The name of the MongoDB collection.

        Returns:
            int: The number of records inserted.
        """
        try:
            client = pymongo.MongoClient(MONGO_DB_URL)
            database = client[database_name]
            collection = database[collection_name]
            result = collection.insert_many(records)
            return len(result.inserted_ids)
        except pymongo.errors.PyMongoError as e:
            raise NetworkSecurityException(e, sys) from e

        
if __name__ == '__main__':
    FILEPATH = "./Network_Data/NetworkData.csv"
    DATABASE = "PhishingDB"
    COLLECTION = "NetworkData"
    nde_obj = NetworkDataExtract()
    records = nde_obj.csv_to_json(FILEPATH)
    records_inserted = nde_obj.push_to_mongo(records, DATABASE, COLLECTION)
    logging.info(f"{records_inserted} records inserted into {DATABASE}.{COLLECTION}")
    

