# from src.utils.to_s3_bucket import save_data_to_s3_bucket
# from moto import mock_aws
# import boto3
# import pytest
# from datetime import datetime
# import re
# import os 
# from botocore.exceptions import ClientError
# @pytest.fixture(autouse=True)
# def aws_credentials():
#     """Mocked AWS Credentials for moto."""
#     os.environ['AWS_ACCESS_KEY_ID'] = 'test'
#     os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'
#     os.environ['AWS_SECURITY_TOKEN'] = 'test'
#     os.environ['AWS_SESSION_TOKEN'] = 'test'
#     os.environ['AWS_DEFAULT_REGION'] = 'eu-west-2'
  
# @pytest.fixture(scope='function')
# def s3():
#     with mock_aws():
#         yield boto3.client('s3', region_name='eu-west-2')

# @pytest.fixture(scope='function', autouse=True)
# def bucket(s3):
#     s3.create_bucket(
#         Bucket='test-bucket',
#         CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'}
#     )

# @pytest.fixture(autouse=True)
# def upload_raw_data(s3, bucket):
#     data ="""first_name,last_name,booking_date,flight_number,departure_airport,arrival_airport,departure_date,return_date,price,currency,booking_status,booking_source,num_passengers
#             1,michelle,cabrera,2025-04-22,LS707,cdg,ams,2025-07-08,2025-08-21,176.67,eur,Cancelled,Website,2
#             2,Jessica,Beard,2025-04-01,LS505,lpa,lon,2025-08-09,,235.32,GBP,cancelled,,1
#             3,sherri,Montgomery,2025-04-14,LS101,CDG,ams,2025-08-11,2025-08-12,216.04,gbp,CANCELLED,mobile,4 
#             """ 
#     now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
#     response = s3.put_object(
#                     Bucket='test-bucket',
#                     Key=f"test_path-{now}.csv",
#                     Body=data

#     ) 
#     return response

# class TestDataIsSavedToS3Bucket():
#     def test_returns_the_correct_type(self, s3, upload_raw_data):
#         assert upload_raw_data['ResponseMetadata']['HTTPStatusCode'] == 200
    
#     def test_s3_bucket_is_not_empty(self, s3):
#         objects = s3.list_objects_v2(Bucket='test-bucket')
#         assert len(objects['Contents']) == 1

#     def test_dates_are_present_in_key(self, s3):    
#         objects = s3.list_objects_v2(Bucket='test-bucket')
#         text = objects['Contents'][0]['Key']
#         assert re.search(r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}\b', text)

#     def test_time_is_present_in_key(self, s3):    
#         objects = s3.list_objects_v2(Bucket='test-bucket')
#         text = objects['Contents'][0]['Key']
#         assert re.search(r'\b([01]\d|2[0-3]):[0-5]\d:[0-5]\d\b',text)
      
#     def test_files_are_in_csv_format(self, s3):    
#         objects = s3.list_objects_v2(Bucket='test-bucket')
#         text = objects['Contents'][0]['Key']
#         assert text.endswith('csv')

#     def test_returns_clienterror(self,s3,upload_raw_data):
#         now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
#         with pytest.raises(ClientError):
#             now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
#             data = """first_name,last_name,booking_date,flight_number,departure_airport,arrival_airport,departure_date,return_date,price,currency,booking_status,booking_source,num_passengers
#             1,michelle,cabrera,2025-04-22,LS707,cdg,ams,2025-07-08,2025-08-21,176.67,eur,Cancelled,Website,2
#             2,Jessica,Beard,2025-04-01,LS505,lpa,lon,2025-08-09,,235.32,GBP,cancelled,,1
#             3,sherri,Montgomery,2025-04-14,LS101,CDG,ams,2025-08-11,2025-08-12,216.04,gbp,CANCELLED,mobile,4 
#             """ 
#             s3.put_object(
#                     Bucket='test_bucket_number2',
#                     Key=f"test_path {now}.csv",
#                     Body=data
#                 )

    
        

 

