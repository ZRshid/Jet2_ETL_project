import pandas as pd 
import logging
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())

def clean_raw_data():
    try:
        r = pd.read_csv('data/raw_data.csv')
        df = pd.DataFrame(r)
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
        df['price']= df['price'].round(0)
       
        conversions_rate=0.88
        index_of_currency_is_eur = df.loc[df['currency'] == 'eur'].index.to_list()
        for each_value in index_of_currency_is_eur:
            df.at[each_value,'price'] = df.at[each_value,'price'] * conversions_rate
        
        new_currency = 'gbp'
        for idx in index_of_currency_is_eur:
            df.at[idx, 'currency'] = new_currency
    
        for col in df.columns:
            if df[col].dtypes == object:
                df[col] = df[col].str.lower()

        logging.info(df.duplicated().sum())
        logging.info(df.describe())
        logging.info(df["booking_date"].isnull().index)
        
        print(df)
               
    except Exception as err:
        raise err


clean_raw_data()


