import os
import sys
import shutil

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.entity.artifact_entity import ModelEvaluationArtifact, ModelPusherArtifact
from networksecurity.entity.config_entity import ModelPusherConfig

from networksecurity.utils.ml_utils.metrics.classification_metrics import get_classification_score
from networksecurity.utils.main_utils.utils import save_object, load_object, write_yaml_file


class ModelPusher:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def initiate_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)