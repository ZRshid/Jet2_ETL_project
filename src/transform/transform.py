from ..utils.get_parquet_file_from_s3 import download_parquet_file_from_s3
from ..utils.convert_file_to_DF import convert_buffer_file_to_df
from ..utils.clean_data import clean_raw_data
import pandas as pd
import os 
import logging 

def transform_data():
    try:
        logging.info('Downloading raw data from the cloud')
        data = download_parquet_file_from_s3(bucket_name=os.getenv('INPUT_BUCKET'), file_path=os.getenv('FILE')) 

        logging.info('Converting data into a Dataframe')
        df = convert_buffer_file_to_df(data)

        logging.info('Cleaning the data')
        cleaned_data = clean_raw_data(df)
        logging.info('The data has now been cleaned and ready for analysis')

        with open("demofile.txt", "w") as f:
            f.write(str(cleaned_data))

        return cleaned_data
    
  
    except Exception as e:
        logging.error(f'Error during transform process: {str(e)}')
        raise

transform_data()

