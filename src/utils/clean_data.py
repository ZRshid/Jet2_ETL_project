import pandas as pd 
from convert_file_to_DF import convert_buffer_file_to_df
from get_parquet_file_from_s3 import download_parquet_file_from_s3
import logging
import os
from dotenv import find_dotenv, load_dotenv
import pyarrow.parquet as pa

import pyarrow.parquet as pq
load_dotenv(find_dotenv())

def clean_raw_data(df):
    """
    Cleans and preprocesses the raw data DataFrame for analysis.

    This function performs the following steps:
    - Fills missing values in columns like 'last_name', 'price', 'booking_source', and 'num_passengers'.
    - Corrects specific rows in 'booking_date', 'flight_number', and 'return_date' with known values.
    - Converts date columns ('booking_date', 'departure_date', 'return_date') to datetime format.
    - Converts 'price' column to numeric type.
    - Converts all string columns to lowercase for consistency.
    - Logs information on duplicate records, data summary, and missing booking dates.
    
    Args:
        df (pd.DataFrame): The raw data DataFrame to clean.
        
    Returns:
        pd.DataFrame: The cleaned and preprocessed DataFrame.
    """

    try:
        df["last_name"]=df["last_name"].fillna("unknown")
        df.at[9 , "booking_date"]="2025-05-10"
        df.at[21 , "booking_date"]="2025-06-06"
        df.at[27 , "booking_date"]="2025-07-02"
        df.at[35 , "booking_date"]="2025-07-13"
        df.at[41 , "booking_date"]="2025-07-26"

        df.at[18 , "flight_number"] ="LS2121"
        df.at[37 , "flight_number"] ="LS2020"

        df.at[1, "return_date"] ="2025-08-21"
        df.at[5 , "return_date"] ="2025-07-06"
        df.at[8 , "return_date"] ="2025-07-02"
        df.at[16 ,"return_date"] ="2025-10-09"

        index_of_missing_price = df[df["price"].isna()].index
        average_price = df["price"].mean()
        for idx in index_of_missing_price:
            df.at[idx ,"price"] = average_price

        index_of_mising_booking_source = df[df["booking_source"].isna()].index
        input_string= 'unknown'
        for idx in index_of_mising_booking_source:
            df.at[idx ,"booking_source"] = input_string

        index_of_mising_number_of_pax = df[df["num_passengers"].isna()].index
        input_value= int(1)
        for idx in index_of_mising_number_of_pax:
            df.at[idx ,"num_passengers"] = input_value

        df['booking_date'] = pd.to_datetime(df['booking_date'])
        df['departure_date'] = pd.to_datetime(df['departure_date'])
        df['return_date'] = pd.to_datetime(df['return_date'])
        df['price'] = pd.to_numeric(df['price'])
    
        for col in df.columns:
            if df[col].dtypes == object:
                df[col] = df[col].str.lower()

        logging.info(df.duplicated().sum())
        logging.info(df.describe())
        logging.info(df["booking_date"].isnull().index)
        return df 
    except Exception as e:
        logging.error(f'Error during data cleaning: {e}')
        raise
 



