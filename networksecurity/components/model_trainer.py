import os
import sys
from xgboost import XGBClassifier

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.utils.main_utils.utils import load_numpy_array_data, load_object, save_object
from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.utils.ml_utils.metrics.classification_metrics import get_classification_score


class ModelTrainer:
    def __init__(self, data_transformation_artifact:DataTransformationArtifact, model_trainer_config:ModelTrainerConfig):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def train_model(self, x_train, y_train):
        try:
            xgb_clf = XGBClassifier()
            xgb_clf.fit(x_train, y_train)
            return xgb_clf
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_model_trainer(self)-> ModelTrainerArtifact:
        try:
            logging.info("Initiating Model Trainer Component")
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path

            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            x_train, y_train, x_test, y_test = (train_arr[:, :-1], train_arr[:, -1], test_arr[:, :-1], test_arr[:, -1])

            model = self.train_model(x_train, y_train)
            y_train_pred = model.predict(x_train)
            classification_train_metrics = get_classification_score(y_true=y_train, y_pred=y_train_pred)

            if classification_train_metrics.f1_score <= self.model_trainer_config.expected_accuracy:
                logging.info("Trained model is not good at provding expected accuracy")

            y_test_pred = model.predict(x_test)
            classification_test_metrics = get_classification_score(y_true=y_test, y_pred=y_test_pred)

            # Overfit and Undefit
            diff = abs(classification_test_metrics.f1_score - classification_train_metrics.f1_score)
            if diff > self.model_trainer_config.overfitting_underfitting_threshold:
                raise Exception("Model is not good, more experimentation needed")
            
            preprocessor = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)

            model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
            os.makedirs(model_dir_path, exist_ok=True)
            network_model = NetworkModel(preprocessor=preprocessor, model=model)
            save_object(self.model_trainer_config.trained_model_file_path, obj=network_model)

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                train_metrics_artifact=classification_train_metrics,
                test_metrics_artifact=classification_test_metrics
            )
            logging.info(f"Model Training Finished, artifact: {model_trainer_artifact}")
            return model_trainer_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)