SELECT 
  departure_airport || ' → ' || arrival_airport as route, 
  ROUND(AVG(return_date - departure_date), 0) as total_days
FROM bookings
WHERE return_date IS NOT NULL
GROUP BY departure_airport, arrival_airport
ORDER BY total_days DESC;