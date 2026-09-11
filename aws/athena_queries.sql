-- TravelFlow Athena Analytics

-- Total bookings and revenue by destination
SELECT
    destination,
    COUNT(*) AS total_bookings,
    SUM(amount) AS total_revenue,
    AVG(amount) AS average_booking_amount
FROM confirmed_bookings
GROUP BY destination
ORDER BY total_revenue DESC;

-- Total revenue
SELECT
    SUM(amount) AS total_revenue
FROM confirmed_bookings;

-- Most popular destinations
SELECT
    destination,
    COUNT(*) AS booking_count
FROM confirmed_bookings
GROUP BY destination
ORDER BY booking_count DESC;