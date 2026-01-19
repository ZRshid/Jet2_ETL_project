import logging
import pandas as pd 
import os

def convert_cleaned_data_to_parquet():
    try:  
        logging.info('Starting CSV → Parquet conversion')
        if os.path.isdir('data'):
            data=pd.read_csv('data/cleaned_data.csv')

            data.to_parquet('cleaned_data.parquet', engine='fastparquet')
            return data 
        else:
            logging.error('Directory does not exist')
    except Exception as error:
        logging.error(f"The following error has occured {error}")
        raise Exception(f"The following error has occured {error}")






