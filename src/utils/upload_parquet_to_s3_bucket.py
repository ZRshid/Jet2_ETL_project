import boto3
import logging 
from botocore.exceptions import ClientError


def upload_parquet_data_to_s3_bucket(bucket_name:str, file_path:str):
    """
    Saves a local file to an S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_path (str): Local file path to upload.

    Returns:
        None

    Raises:
        ClientError: If an error occurs during upload.
    """
    s3_client = boto3.client("s3", region_name='eu-west-2')
    try:
       
        logging.info(f"Starting the process of uploading data into the following {bucket_name}")
        s3_client.upload_file(
            Bucket=bucket_name, 
            Filename=file_path,
            Key=f"{file_path}")
        logging.info(f"You have successsfully uploaded data to the {bucket_name} bucket")
    except ClientError as e:
        logging.error(f"The following error has occured {e}")
        raise ClientError(f"The following {e.response} has taken place")
