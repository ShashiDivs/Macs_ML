import sys,os
from dataclasses import dataclass
from pathlib import Path
from src.exception.exception import CustomException
from src.logger.logging import logging
import pandas as pd 
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def intiated_data_ingestion(self):
        logging.info("Data Ingestion Begins Here.....")
        try:
            data = pd.read_csv("/config/workspace/experiments/gemstone.csv")
            logging.info("Reading the DataFramework...")


            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info(" i have saved the raw dataset in artifact folder")
            
            logging.info("here i have performed train test split")

            train_data,test_data = train_test_split(data,test_size=0.25)
            logging.info("train test split completed")

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info(f"data ingestion part completed Traindta shape is {train_data.shape} Testdata shape is {test_data.shape}")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("The error occured")
            raise CustomException(e,sys) from e 


if __name__ == "__main__":
    obj = DataIngestion()
    obj.intiated_data_ingestion()