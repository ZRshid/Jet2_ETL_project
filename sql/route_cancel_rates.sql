WITH
cte1 as (
  SELECT ROUND(SUM(price * num_passengers),2) as total_revenue, 
         departure_airport || ' --> ' || arrival_airport as route
  FROM bookings
  GROUP BY departure_airport, arrival_airport
),
cte2 as (
  SELECT ROUND(SUM(price * num_passengers),2) as lost_revenue, 
         departure_airport || ' --> ' || arrival_airport as route
  FROM bookings
  WHERE booking_status = 'cancelled'
  GROUP BY departure_airport, arrival_airport
)
SELECT cte2.route,
       cte1.total_revenue,
       cte2.lost_revenue, 
       ROUND((cte2.lost_revenue / cte1.total_revenue * 100),2) as cancel_pct
FROM cte1
JOIN cte2 on cte1.route = cte2.route
ORDER BY cancel_pct desc;