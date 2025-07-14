from src.extract.extract import to_csv
import pytest
import csv


def test_empty_input():
    test_file = "data/test_temp.csv"
    result = to_csv([], test_file)
    expected_results = "status: success, rows_written: 0 rows"
    assert result == expected_results
    
def test_checks_the_correct_header_are_present():
    with open("data/raw_data.csv", mode="r", newline='', encoding="utf-8") as file:
        content = file.read()
        for headers in ["id","first_name","booking_date","flight_number","departure_airport","arrival_airport","departure_date"]:
            assert headers in content
        
        assert "1,michelle,cabrera,2025-04-22,LS707,cdg,ams,2025-07-08,2025-08-21,176.67,eur,Cancelled,Website,2" in content

def test_checks_the_correct_info_is_present():
    with open("data/raw_data.csv", mode="r", newline='', encoding="utf-8") as file:
        content =list(csv.DictReader(file))
        assert content[0] == {'id': '1', 'first_name': 'michelle', 'last_name': 'cabrera', 'booking_date': '2025-04-22', 
                              'flight_number': 'LS707', 'departure_airport': 'cdg', 'arrival_airport': 'ams', 'departure_date': '2025-07-08', 
                              'return_date': '2025-08-21', 'price': '176.67', 'currency': 'eur', 'booking_status': 'Cancelled', 'booking_source': 'Website',
                              'num_passengers': '2'}

def test_return_the_correct_number_of_rows():
    with open("data/raw_data.csv", mode="r", newline='', encoding="utf-8") as file:
        content =list(csv.DictReader(file))
        assert content[0]['id'] == '1'
        assert content[-1]['id'] == '44'
         
def test_returns_an_exception():
    with pytest.raises(Exception):
        to_csv("not a list", "test.csv")
