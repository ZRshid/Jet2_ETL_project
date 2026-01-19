SELECT 
  ROUND((SUM(CASE WHEN booking_status = 'cancelled' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)), 1) as cancel_rate_pct
FROM bookings;