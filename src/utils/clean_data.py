import pandas as pd 
from get_parquet_file_from_s3 import download_parquet_file_from_s3
from convert_file_to_DF import convert_buffer_file_to_df
import io
import os


def clean_raw_data():
    data = download_parquet_file_from_s3(bucket_name=os.getenv('INPUT_BUCKET'), file_path=os.getenv('FILE_KEY'))

    df = convert_buffer_file_to_df(data)

    missing_booking = df["booking_date"].isnull()
    print(missing_booking)
    41

    df["last_name"]=df["last_name"].fillna("unknown")
    df.at[9 , "booking_date"] ="2025-05-10"
    df.at[21 , "booking_date"] ="2025-06-06"
    df.at[27 , "booking_date"] ="2025-07-02"
    df.at[35 , "booking_date"] ="2025-07-13"
    df.at[41 , "booking_date"] ="2025-07-26"

    df.at[18 , "flight_number"] ="LS2121"
    df.at[37 , "flight_number"] ="LS2020"


    df.at[1, "return_date"] ="2025-08-21"
    df.at[5 , "return_date"] ="2025-07-06"
    df.at[8 , "return_date"] ="2025-07-02"
    df.at[16 , "return_date"] ="2025-10-09"
  

    df['booking_date'] = pd.to_datetime(df['booking_date'])
    df['departure_date'] = pd.to_datetime(df['departure_date'])
    df['return_date'] = pd.to_datetime(df['return_date'])
    df['price'] = pd.to_numeric(df['price'])
    df.duplicated().sum()
    df.columns = df.columns.str.lower()


    missing_vlaues = df.isnull().sum()
    print(missing_vlaues)

    print(df)

    return df 





   
clean_raw_data()


