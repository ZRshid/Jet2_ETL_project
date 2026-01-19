WITH
total_by_source AS (
  SELECT booking_source, COUNT(*) as total_bookings
  FROM bookings
  GROUP BY booking_source
),
confirmed_by_source AS (
  SELECT booking_source, COUNT(*) as confirmed_bookings
  FROM bookings
  WHERE booking_status = 'confirmed'
  GROUP BY booking_source
)
SELECT
  t.booking_source,
  t.total_bookings,
  c.confirmed_bookings,
  ROUND(c.confirmed_bookings * 100.0 / t.total_bookings, 1) AS conversion_rate
FROM total_by_source t
JOIN confirmed_by_source c ON t.booking_source = c.booking_source
ORDER BY conversion_rate DESC;
