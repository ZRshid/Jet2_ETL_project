# import psycopg2
# import os 
# from dotenv import find_dotenv, load_dotenv

# load_dotenv(find_dotenv())
# def seed_db():
#     conn = None
#     cursor = None
#     try:
#         conn = psycopg2.connect(
#             dbname=os.getenv('PG_DATABASE_test'),
#             user=os.getenv("PG_USER_"),
#             password=os.getenv("PG_PASSWORD"),
#             host=os.getenv("PG_HOST"),
#             port=os.getenv("PG_PORT")
#         )
       
#         cursor = conn.cursor()
#         cursor.execute("DROP TABLE IF EXISTS booking_test;")
#         cursor.execute("""CREATE TABLE booking_test (
#                         id SERIAL PRIMARY KEY,
#                         first_name TEXT NOT NULL,
#                         last_name TEXT NOT NULL,
#                         booking_date DATE NOT NULL,
#                         flight_number VARCHAR(10) NOT NULL,
#                         departure_airport VARCHAR(5) NOT NULL,
#                         arrival_airport VARCHAR(5) NOT NULL,
#                         departure_date DATE NOT NULL,
#                         return_date DATE,
#                         price DECIMAL(10, 2),
#                         currency VARCHAR(5),
#                         booking_status VARCHAR(20),
#                         booking_source VARCHAR(20),
#                         num_passengers INTEGER
#                     );
#                     """)
#         insert_query_booking = """INSERT INTO booking_test (id,first_name,last_name,booking_date,flight_number,departure_airport,arrival_airport,departure_date,
#                                 return_date,
#                                 price,
#                                 currency,
#                                 booking_status,
#                                 booking_source,
#                                 num_passengers
#                                 )
#                             VALUES 
                                                
#                             (DEFAULT, 'Alice', 'Smith', '2025-05-15', 'CD456', 'LAX', 'ORD', '2025-06-10', '2025-06-15', 420.00, 'USD', 'Confirmed', 'Mobile', 1),
#                             (DEFAULT, 'Bob', 'Johnson', '2025-04-20', 'EF789', 'ORD', 'MIA', '2025-07-01', '2025-07-05', 310.75, 'USD', 'Cancelled', 'Website', 3),
#                             (DEFAULT, 'Carla', 'Mendez', '2025-03-30', 'GH012', 'MIA', 'SEA', '2025-08-10', '2025-08-20', 580.25, 'USD', 'Confirmed', 'Agent', 2),
#                             (DEFAULT, 'David', 'Lee', '2025-06-10', 'IJ345', 'SEA', 'DEN', '2025-09-05', '2025-09-15', 450.00, 'USD', 'Confirmed', 'Mobile', 1),
#                             (DEFAULT, 'Elena', 'Patel', '2025-03-20', 'KL678', 'DFW', 'DEN', '2025-07-01', '2025-07-10', 275.25, 'USD', 'Cancelled', 'Mobile', 1),
#                             (DEFAULT, 'Frank', 'Connor', '2025-04-12', 'MN901', 'DEN', 'LAX', '2025-08-15', '2025-08-25', 530.40, 'USD', 'Confirmed', 'Website', 2),
#                             (DEFAULT, 'Grace', 'Wong', '2025-05-01', 'OP234', 'ORD', 'JFK', '2025-06-20', '2025-06-22', 210.00, 'USD', 'Confirmed', 'Agent', 1),
#                             (DEFAULT, 'Hiroshi','Tanaka', '2025-06-02', 'QR567', 'JFK', 'SFO', '2025-07-30', '2025-08-05', 650.50, 'USD', 'Cancelled', 'Mobile', 4),
#                             (DEFAULT, 'Isabel', 'Garcia', '2025-05-25', 'ST890', 'SFO', 'LAS', '2025-09-10', '2025-09-15', 295.75, 'USD', 'Confirmed', 'Website', 1),
#                             (DEFAULT, 'Jason', 'Kim', '2025-07-01', 'UV123', 'LAS', 'MIA', '2025-10-01', '2025-10-10', 710.00, 'USD', 'Confirmed', 'Agent', 3);
                            
#                             """
#         cursor.execute(insert_query_booking)
#         conn.commit()
#         cursor.execute("SELECT * FROM booking_test")
#         description = cursor.description
#         column_names = [col[0] for col in description]
#         data = [dict(zip(column_names, row))  
#                 for row in cursor.fetchall()]
#         return data
#     except Exception as e:
#         print(f"error:{e}")
#     finally:
#         if cursor is not None:
#             cursor.close()
#         if conn is not None:
#             conn.close()

# seed_db()

    

   