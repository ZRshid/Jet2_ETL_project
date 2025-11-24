from ..utils.db_conn import conn_database
from ..utils.to_parquet import to_parquet
from ..utils.to_s3_bucket import save_data_to_s3_bucket
import logging
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def extract_data():
    try:
        logging.info('The extraction process has started')
        df = conn_database()
        logging.info('Database connection successful, data extracted')
        
        to_parquet(df)
        logging.info('Extracted data saved in Parquet format')
        
        save_data_to_s3_bucket(bucket_name=os.getenv('INPUT_BUCKET'), file_path=os.getenv('FILE'))
        logging.info(f'data saved to s3 bucket')
    except Exception as e:
        logging.error()

extract_data()














