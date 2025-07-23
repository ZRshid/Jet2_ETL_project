from src.utils.to_s3_bucket import save_data_to_s3_bucket
from moto import mock_aws
import boto3
import pytest
import os 

@pytest.fixture(autouse=True)
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'test'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'
    os.environ['AWS_SECURITY_TOKEN'] = 'test'
    os.environ['AWS_SESSION_TOKEN'] = 'test'
    os.environ['AWS_DEFAULT_REGION'] = 'eu-west-2'
  
@pytest.fixture(scope='function')
def s3():
    with mock_aws():
        yield boto3.client('s3', region_name='eu-west-2')

@pytest.fixture(scope='function', autouse=True)
def bucket(s3):
    s3.create_bucket(
        Bucket='test-bucket',
        CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'}
    )

@pytest.fixture(autouse=True)
def raw_data(s3):
    data ="""first_name,last_name,booking_date,flight_number,departure_airport,arrival_airport,departure_date,return_date,price,currency,booking_status,booking_source,num_passengers
            1,michelle,cabrera,2025-04-22,LS707,cdg,ams,2025-07-08,2025-08-21,176.67,eur,Cancelled,Website,2
            2,Jessica,Beard,2025-04-01,LS505,lpa,lon,2025-08-09,,235.32,GBP,cancelled,,1
            3,sherri,Montgomery,2025-04-14,LS101,CDG,ams,2025-08-11,2025-08-12,216.04,gbp,CANCELLED,mobile,4 
            """
    return data
class TestDataIsSavedToS3Bucket():
    def test_returns_the_correct_type(self, s3, raw_data):
        assert isinstance(raw_data, str)







