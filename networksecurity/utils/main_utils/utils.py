import os
import sys

import yaml
import dill
import pickle
import numpy as np
import pandas as pd


from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


def read_yaml_file(file_path: str):
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    

def write_yaml_file(file_path: str, content: object, repalce: bool = False):
    try:
        if repalce:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    

def save_numpy_array_data(file_path: str, array: np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    

def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info(f"Saving Object at {file_path}")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"Object saved at {file_path}")
    except Exception as e:
        raise NetworkSecurityException(e, sys)