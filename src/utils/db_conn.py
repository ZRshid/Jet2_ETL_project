import psycopg2
from io import BytesIO
import os 
from dotenv import find_dotenv, load_dotenv
import logging
import pandas as pd

load_dotenv(find_dotenv())

def conn_database():
    """
    This function reads database credentials from env variables and connects to the required database which allows the extraction of data to occur.
    """
    try:
       
        logging.info("Initiating DB connection")
        conn = psycopg2.connect(
            dbname=os.getenv('PG_DATABASE'),
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD"),
            host=os.getenv("PG_HOST"),
            port=os.getenv("PG_PORT")
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jet2_bookings")
        rows = cursor.fetchall()

        data=[row for row in rows]
        names_of_columns = [col[0] for col in cursor.description]

        df  = pd.DataFrame(list(data))
        df.columns = names_of_columns
                       
      
        logging.info("You have succesfully extracted data from the db")
        return df

    except Exception as error:
        logging.error(f"The following error has occured {error}")
        raise Exception(f"The following error has occured {error}")
    finally:
       cursor.close()
       conn.close()


       
if __name__ == "__main__":
    conn_database()
 