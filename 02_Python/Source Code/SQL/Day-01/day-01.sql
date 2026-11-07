SELECT COUNT(*) AS total_trips   -- counts every row
FROM trips;

SHOW DATABASES LIKE 'bike%';

USE bike_analytics;
SHOW TABLES;

DESCRIBE trips;

DESCRIBE stations;

SELECT trip_id, bike_type, minutes, fee_inr FROM trips ORDER BY trip_id LIMIT 5;

SELECT * FROM stations;

SELECT trip_id AS `Trip ID`, fee_inr AS `Fee (INR)` FROM trips LIMIT 3;

SELECT DISTINCT bike_type FROM trips ORDER BY bike_type;

SELECT COUNT(*) AS all_rows, COUNT(DISTINCT trip_id) AS unique_trip_ids, COUNT(DISTINCT bike_id) AS bikes FROM trips;

SELECT COUNT(*) AS all_rows, COUNT(NULLIF(status, 'cancelled')) AS not_cancelled FROM trips;

SELECT COUNT(*) AS trips, ROUND(SUM(fee_inr), 2) AS revenue_inr FROM trips;

SELECT MIN(started_at) AS first_trip, MAX(started_at) AS last_trip, COUNT(DISTINCT DATE(started_at)) AS days_with_trips FROM trips;

SELECT name, zone, opened FROM stations ORDER BY opened, name;