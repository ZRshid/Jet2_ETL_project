SELECT 
    COUNT(*) as bookings,  
    booking_status, 
    ROUND(SUM(price * num_passengers),2) as total
FROM bookings
GROUP BY booking_status
