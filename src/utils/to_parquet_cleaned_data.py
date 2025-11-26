from clean_data import clean_raw_data
import logging
import pandas as pd 

def convert_cleaned_data_to_parquet():
    df=clean_raw_data()
    to_parquet=df.to_parquet("cleaned_data")
    df_parquet = pd.read_parquet("data/cleaned_data")
  
    logging.info(f'Data has been converted to parquet format {df_parquet} and is now ready to be stroed in the cloud')
    return to_parquet
convert_cleaned_data_to_parquet()

    
