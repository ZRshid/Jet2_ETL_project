
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import logging 

def save_data_to_s3_bucket(bucket_name:str, file_path:str):

    """
    Saves data to an S3 bucket.
    Args:
        data (str): The data to be saved, in CSV format.
        bucket_name (str): The name of the S3 bucket where the data will be stored.
    Returns:
        None
    Raises:
        clienterror: If there is an error during the S3 upload.
    """

    s3_client = boto3.client("s3", region_name='eu-west-2')
    try:
        logging.info(f"Starting the process of uploading data into the following {bucket_name}")

        now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        s3_client.upload_file(
            Bucket=bucket_name, 
            Filename=file_path,  
            Key=f"{file_path}{now}")
        logging.info(f"You have successsfully uploaded data to the {bucket_name} bucket")
    except ClientError as error:
        logging.error(f"The following error has occured {error}")
        raise ClientError(f"The following {error.response} has taken place")

if __name__ == "main":
    save_data_to_s3_bucket()
  
