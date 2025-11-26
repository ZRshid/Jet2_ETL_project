from ..utils.upload_parquet_to_s3_bucket import upload_parquet_data_to_s3_bucket
import logging
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def load_data():
    logging.info('Uploading processed data to the cloud')
    try:
        data= upload_parquet_data_to_s3_bucket(bucket_name=os.getenv('OUTPUT_BUCKET'), file_path=os.getenv('PROCESSED_FILE')) 
        return data
    except Exception as e:
        logging.error(f'Error during the load porcess: {e}')
        raise
load_data()

