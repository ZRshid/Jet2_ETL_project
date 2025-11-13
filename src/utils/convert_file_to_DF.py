from ..utils.get_parquet_file_from_s3 import download_parquet_file_from_s3
import pyarrow.parquet as pq 
import os 
import logging 


def convert_buffer_file_to_df():
    """
    Downloads the buffer (data stored in memory) to a dataframe. 
    Args:
        buffer: This is the data stored in memory. 
    Returns:
         A Dataframe.   
    Raises:
         Exception: If there is an exception when converting the files into a dataframe, an exception is raised. 
    """
    
    data=download_parquet_file_from_s3(bucket_name=os.getenv('INPUT_BUCKET'), file_path=os.getenv('FILE_KEY'))

    try:
        table = pq.read_table(data) #reads files. Bytes Io makes the data behave like a file hence it can be used here. 
        df = table.to_pandas()
        print(f"success {df}")
    except Exception as error:
        logging.error(f"error: The file could not be {error}")
        raise error
                      
convert_buffer_file_to_df()





