import boto3
import io
import logging
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

def download_parquet_file_from_s3(bucket_name:str, file_path:str):
    """
    Downloads data in parquet format from an S3 bucket.

    Args:
        bucket_name (str): The S3 bucket name.
        file_path (str): The path/key to the parquet file in the bucket.

    Returns:
        BytesIO: In-memory bytes buffer containing the parquet file data.

    Raises:
        Exception: If there is an error when downloading from S3.
    """

    s3_client = boto3.client("s3", region_name='eu-west-2')
    try:
        
        logging.info(f"Starting download of {file_path} from bucket {bucket_name}")
        response = s3_client.get_object(Bucket=bucket_name,Key=file_path)
        buffer = io.BytesIO(response['Body'].read())  #in memory, not on disk
        logging.info(f"Successfully downloaded {file_path} from bucket {bucket_name}")
        return buffer
    except Exception as e:
        logging.error(f"Error downloading {file_path} from bucket {bucket_name}: {e}")
        raise e
