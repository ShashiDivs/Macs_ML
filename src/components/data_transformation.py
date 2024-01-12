import sys,os
from dataclasses import dataclasses
from pathlib import Path
from src.exception.exception import CustomException
from src.logger.logging import logging
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

class DataTransformationConfig:
    pass


class DataTransformation:
    def __init__(self):
        pass

    def intiated_data_transform(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)