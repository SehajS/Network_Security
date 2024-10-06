import os
import sys
import numpy as np
import pandas as pd


"""
Common constant variables for training pipeline
"""
PIPELINE_NAME = "NetworkSecurity"
ARTIFACT_DIR = "Artifacts"
FILE_NAME = "NetworkData.csv"

TARGET_COLUMN = "Result"

TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"

SAVED_MODEL_DIR = os.path.join("saved_models")


"""
Data Ingestion related constants
"""
DATA_INGESTION_DATABASE_NAME = "PhishingDB"
DATA_INGESTION_COLLECTION_NAME = "NetworkData"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2


"""
Data Validation related constants
"""


"""
Data Transformation related constants
"""


"""
Model Trainer related constants
"""


"""
Model Evaluation related constants
"""


"""
Model Pusher related constants
"""