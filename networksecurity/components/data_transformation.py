import os
import sys
import numpy as np
import pandas as pd

from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.utils.main_utils.utils import save_numpy_array_data, save_object

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
    
    def get_data_transformer_object(self):
        logging.info("Entered get_transformer_object method of DataTransformation class")

        try:
            imputer: KNNImputer = KNNImputer(
                **training_pipeline.DATA_TRANSFORMATION_IMPUTER_PARAMS
            )
            logging.info(f"Initialized KNN Imputer with params: {training_pipeline.DATA_TRANSFORMATION_IMPUTER_PARAMS}")
            preprocessor: Pipeline = Pipeline(
                [("imputer", imputer)]
            )
            return preprocessor
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def initiate_data_transformation(self) -> DataTransformationArtifact:
        logging.info("Initiating Data Transformation Component")

        try:
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)

            preprocessor = self.get_data_transformer_object()

            # prepare training dataframes by separating target_column
            input_feature_train_df = train_df.drop(columns=[training_pipeline.TARGET_COLUMN])
            target_feature_train_df = train_df[training_pipeline.TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1, 0)

            # prepare testing dataframes by separating target_column
            input_feature_test_df = test_df.drop(columns=[training_pipeline.TARGET_COLUMN])
            target_feature_test_df = test_df[training_pipeline.TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1, 0)

            # Fit the preprocessor on train data and transform the test data
            preprocessor_obj = preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature = preprocessor_obj.transform(input_feature_train_df)
            transformed_input_test_feature = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[transformed_input_train_feature, np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_input_test_feature, np.array(target_feature_test_df)]

            # save train_arr and test_arr
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, array=train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, array=test_arr)
            # save the preprocessor object as well
            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor_obj)

            data_transformation_artifact = DataTransformationArtifact(
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path
            )
            logging.info(f"Data Transformation Completed, artifacts: {data_transformation_artifact}")
            return data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)