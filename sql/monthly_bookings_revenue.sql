SELECT 
  EXTRACT(MONTH FROM booking_date) as booking_month, 
  COUNT(*) as bookings, 
  ROUND(SUM(price * num_passengers), 2) AS revenue
FROM bookings
GROUP BY booking_month
ORDER BY booking_month;
