from ..utils.db_conn import conn_database
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import logging


def to_parquet(df:pd.DataFrame):
    """
    Fetches data from a databse thats been converted into a DataFrame. 
    Args:
        df(pd:DataFrame): Df that will be converted to parquet format.
    Returns:
         Returns data that is in parquet format.
    Raises:
        Exception: If there is an exception when saving when converting DF
    """
    try:
        logging.info("Starting the process of converting DF into parquet format")
        df.to_parquet('output.parquet', engine='pyarrow', index=False)
        logging.info('Data has been succesfully converted to parquet format')
    except Exception as error:
        logging.error(f'The following error has occured {error}')
        raise error
       
if __name__ == "__main__":
    to_parquet()