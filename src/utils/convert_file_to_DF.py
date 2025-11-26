import pyarrow.parquet as pq 
import logging 

def convert_buffer_file_to_df(data):
    """
    Downloads the buffer (data stored in memory) to a dataframe. 
    Args:
        buffer: This is the data stored in memory. 
    Returns:
         A Dataframe.   
    Raises:
         Exception: If there is an exception when converting the files into a dataframe, an exception is raised. 
    """
    
    try:
        table = pq.read_table(data) 
        df = table.to_pandas()
        return df
    except Exception as e:
        logging.error(f"error: The file could not be {e}")
        raise e
                      






    