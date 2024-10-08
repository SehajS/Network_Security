import os
import sys
import pandas as pd

from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact

from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


class DataValidation:
    def __init__(self):
        pass
    
    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def validate_number_of_columns(self, dataframe: pd.DataFrame)-> bool:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def is_numerical_column_exist(self, dataframe: pd.DataFrame)-> bool:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def detect_dataset_drift(self, base_df, current_df, threshold=0.05) -> bool:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            self.read_data()
            self.validate_number_of_columns()
            self.detect_dataset_drift()
        except Exception as e:
            raise NetworkSecurityException(e, sys)
