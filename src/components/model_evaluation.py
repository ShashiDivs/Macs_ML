import sys,os
from dataclasses import dataclasses
from pathlib import Path
from sklearn.model_selection import train_train_splits
from src.exception.exception import CustomException
from src.logger.logging import logging

class ModelEvaluationConfig:
    pass


class ModelEvaluation:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)