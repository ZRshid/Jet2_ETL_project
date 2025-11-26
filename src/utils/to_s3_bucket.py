
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import logging 

def save_data_to_s3_bucket(bucket_name:str, file_path:str):
    """
    Saves a local file to an S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_path (str): Local path to the file to upload.

    Returns:
        None

    Raises:
        ClientError: If there is an error during the upload.
    """

    s3_client = boto3.client("s3", region_name='eu-west-2')
    try:
        logging.info(f"Starting the process of uploading data into the following bucket:{bucket_name}")

        now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        key = f"{file_path}"
        s3_client.upload_file(
            Bucket=bucket_name, 
            Filename=file_path,  
            Key=key)
        logging.info(f"Successfully uploaded {file_path} to bucket {bucket_name} as {key}")
    
    except ClientError as error:
        logging.error(f"The following error has occured {error}")
        raise ClientError(f"The following {error.response} has taken place")

if __name__ == "main":
    save_data_to_s3_bucket()
  
