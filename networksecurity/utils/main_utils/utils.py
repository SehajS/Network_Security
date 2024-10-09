import os
import sys

import yaml
import dill
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