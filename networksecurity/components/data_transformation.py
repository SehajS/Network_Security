import os
import sys
import numpy as np
import pandas as pd

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.constant import training_pipeline
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.entity.artifact_entity import DataValidationArtifact, DataTransformationArtifact



class DataTransformation:
    def __init__(self, data_validation_artifact: DataValidationArtifact, data_transformation_config: DataTransformationConfig):
        try:
            self.data_validation_artifact: DataValidationArtifact = data_validation_artifact
            self.data_transformation_config: DataTransformationConfig = data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def initiate_data_transformation(self) -> DataTransformationArtifact:
        logging.info("Initiating Data Transformation Pipeline")

        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)