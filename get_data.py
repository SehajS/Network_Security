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
    
    def csv_to_json(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def push_to_mongo(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

