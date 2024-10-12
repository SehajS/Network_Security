import os
import sys
import pandas as pd

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact, ModelEvaluationArtifact
from networksecurity.entity.config_entity import ModelEvaluationConfig
from networksecurity.utils.ml_utils.metrics.classification_metrics import get_classification_score
from networksecurity.utils.ml_utils.model.estimator import NetworkModel, ModelResovler
from networksecurity.utils.main_utils.utils import load_object, save_object, read_yaml_file
from networksecurity.constant import training_pipeline


class ModelEvaluation:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def initiate_model_evalution(self)-> ModelEvaluationArtifact:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)