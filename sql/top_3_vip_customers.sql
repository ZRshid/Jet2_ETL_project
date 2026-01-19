SELECT 
  first_name || ' ' || last_name as customer, 
  ROUND(SUM(price * num_passengers), 2) as total_spend
FROM bookings
GROUP BY first_name, last_name
ORDER BY total_spend DESC 
LIMIT 3;