from ..utils.db_conn import conn_database
from ..utils.to_csv import to_csv
from ..utils.to_s3_bucket import save_data_to_s3_bucket

def extracts_data():
    print('The extraction process has started')

    first = conn_database()

    print('conn to databse was succesfull, data has been ectracted')


    print('extracted data converted into parquet format')

    to_csv(first)

    print('data conversion was succesfull')

    print('extracted data saved to s3 bucket')

    save_data_to_s3_bucket("raw-data20251024115502095400000002", '/Project/Jet2_ETL_project/output.parquet')

    print('data saved to s3')


extracts_data()














