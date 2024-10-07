import os
import sys
import pandas as pd
import numpy as np
import pymongo
from dotenv import load_dotenv

from sklearn.model_selection import train_test_split

from networksecurity.logger.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact


load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def export_collection_as_dataframe(self):
        try:
            db_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name

            self.mongo_client =pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[db_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            
            if "_id" in df.columns:
                df = df.drop(columns=["_id"])
            
            df = df.replace({"na": np.nan})
            return df
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def export_data_to_feature_store(self, dataframe: pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            logging.info(f"Feature Store created at {feature_store_file_path}")
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def split_data_into_train_test_sets(self, dataframe: pd.DataFrame) -> None:
        """
        Split the given dataframe into training and test sets.

        Args:
            dataframe (pd.DataFrame): The dataframe to be split.

        Returns:
            None
        """
        try:
            logging.info(f"Performing train test split on the dataframe of {dataframe.shape[0]} records")
            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.train_test_split_ratio,
                random_state=42
            )
            logging.info(f"Splitting done. Train: {train_set.shape[0]} and Test: {dataframe.shape[0]} records")

            train_file_path = self.data_ingestion_config.training_file_path
            test_file_path = self.data_ingestion_config.testing_file_path

            logging.info(f"Exporting train and test file path: {train_file_path} and {test_file_path}")
            os.makedirs(os.path.dirname(train_file_path), exist_ok=True)

            train_set.to_csv(train_file_path, index=False)
            test_set.to_csv(test_file_path, index=False)
            logging.info("Exported train and test files")
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    
    def initiate_data_ingestion(self):
        try:
            df = self.export_collection_as_dataframe()
            df = self.export_data_to_feature_store(df)
            self.split_data_into_train_test_sets(df)

            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path, test_file_path=self.data_ingestion_config.testing_file_path)
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    