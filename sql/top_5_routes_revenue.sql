SELECT 
  departure_airport, 
  arrival_airport, 
  ROUND(SUM(price * num_passengers), 2) as total_revenue
FROM bookings
GROUP BY departure_airport, arrival_airport
ORDER BY total_revenue DESC 
LIMIT 5;


