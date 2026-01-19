SELECT 
  ROUND(SUM(price * num_passengers), 2) as revenue, 
  booking_source
FROM bookings
GROUP BY booking_source
ORDER BY revenue DESC;