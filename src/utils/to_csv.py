from src.utils.db_conn import conn_database
import logging 
import csv

def to_csv(data:list[dict],file_path)-> str :

    """
    Takes data from a databse in dict format. 
    Args:
        data (dict): The data that will be converted to csv format 
    Returns:
        A Buffer: Essentially stores the files in memory and not on disk.
    Raises:
        Exception: If there is an exception when downloading the files and saving it in memory, an exception is raised.
    """
    try:
        logging.info("Initiating the process of converting  raw data to csv format")
        with open(file_path, mode="w", newline='', encoding="utf-8") as file:
            fieldnames = [
                    "id",
                    "first_name",
                    "last_name",
                    "booking_date",
                    "flight_number",
                    "departure_airport",
                    "arrival_airport",
                    "departure_date",
                    "return_date",
                    "price",
                    "currency",
                    "booking_status",
                    "booking_source",
                    "num_passengers"
                ]
            csv_writer = csv.DictWriter(file,fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(data)
           
            return f"status: success, rows_written: {len(data)} rows"    
    except Exception as error:
        logging.error(f"The following error has occured {error}")
        raise Exception(f"The following error has occured {error}")
    
if __name__ == "__main__":
    initial = conn_database()
    second = to_csv(initial,"/home/zakii/Project/Jet2_ETL_project/data/raw_data.csv")