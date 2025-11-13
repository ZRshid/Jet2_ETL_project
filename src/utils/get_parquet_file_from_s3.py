import boto3
import io
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

def download_parquet_file_from_s3(bucket_name:str, file_path:str):
    """
    Downloads data in parquet from an S3 bucket. 
    Args:
        bucket_name:str: The name of the Bucket where the data is strored.
    Returns:
         Returns data that is in parquet format.
    Raises:
        Exception: If there is an exception when downloading data from the S3 Bucket"""

    s3_client = boto3.client("s3", region_name='eu-west-2')
    try:
        response = s3_client.get_object(Bucket=bucket_name,Key=file_path)
        buffer = io.BytesIO(response['Body'].read())  #in memory, not on disk
        return buffer
    except Exception as error:
        print(f'The following error has occured {error}')


