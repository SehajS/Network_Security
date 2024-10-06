from datetime import datetime
import os

from networksecurity.constant import training_pipeline


print(training_pipeline.ARTIFACT_DIR)


class TrainingPipelineConfig:
    def __init__(self, timestamp: datetime = datetime.now()) -> None:
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_dir = os.path.join(
            training_pipeline.ARTIFACT_DIR, timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        )
        self.timestamp = timestamp

class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_dir = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
        )
        self.training_file_path = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
        )
        self.testing_file_path = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
        )
        self.train_test_split_ratio = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.database_name = training_pipeline.DATA_INGESTION_DATABASE_NAME
        self.collection_name = training_pipeline.DATA_INGESTION_COLLECTION_NAME


class DataValidationConfig:
    def __init__(self):
        pass


class DataTransformationConfig:
    def __init__(self):
        pass


class ModelTrainerConfig:
    def __init__(self):
        pass


class ModelEvaluationConfig:
    def __init__(self):
        pass


class ModelPusherConfig:
    def __init__(self):
        pass