# import pytest
# from tests.extract.integration_testing.seed_db import seed_db
# import datetime
# import decimal

# @pytest.fixture(autouse=True)
# def autoseeddb():
#     seed_db()

# def testreturnsthecorrectnumbeofcolumns():
#         expected_length = 14
#         result = seed_db()
#         assert len(result[0]) == expected_length

# def test_checks_whether_the_correct_data_types_are_present():
#         result = seed_db()
#         for row in result:
#             assert isinstance(row["id"], int)
#             assert isinstance(row["first_name"], str)
#             assert isinstance(row["last_name"], str)
#             assert isinstance(row["booking_date"],datetime.date)
#             assert isinstance(row["flight_number"], str)
#             assert isinstance(row["departure_airport"], str)
#             assert isinstance(row["departure_date"], datetime.date)
#             assert isinstance(row["return_date"], datetime.date)
#             assert isinstance(row["price"], decimal.Decimal)
#             assert isinstance(row["currency"], str)
#             assert isinstance(row["booking_status"], str)
#             assert isinstance(row["booking_source"], str)
#             assert isinstance(row["num_passengers"], int)
     
# def test_checks_whether_the_first_input_matches():
#         excpected_results = {'id': 1, 'first_name': 'Alice', 'last_name': 'Smith', 'booking_date': datetime.date(2025, 5, 15),
#                             'flight_number': 'CD456', 'departure_airport': 'LAX', 'arrival_airport': 'ORD', 'departure_date': datetime.date(2025, 6, 10), 
#                             'return_date': datetime.date(2025, 6, 15), 'price': decimal.Decimal('420.00'), 'currency': 'USD', 'booking_status': 'Confirmed', 
#                             'booking_source': 'Mobile', 'num_passengers': 1}
#         result = seed_db()
#         assert result[0] == excpected_results
