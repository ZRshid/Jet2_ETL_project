import logging
from src.extract.extract import extract_data
from src.transform.transform import transform_data
from src.load.load import load_data


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def orchestrate_etl():
    try:
        logging.info("ETL process started")
        
        logging.info("Starting extraction phase")
        extract_data()
        logging.info("Extraction phase completed")
        
        logging.info("Starting transformation phase")
        transform_data()
        logging.info("Transformation phase completed")

        logging.info("Starting load phase")
        load_data()
        logging.info("Load phase completed")
        
        logging.info("ETL process finished")
    except Exception as e:
        logging.error(f'Error during ETL process: {str(e)}')
        raise
  

orchestrate_etl()