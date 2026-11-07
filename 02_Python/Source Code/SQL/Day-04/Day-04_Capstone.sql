USE bike_analytics;

SELECT start_station, 
       COUNT(*) AS departures, 
       SUM(status = 'completed') AS completed, 
       ROUND(SUM(fee_inr),2) AS revenue, 
       ROUND(SUM(fee_inr) / SUM(status = 'completed'), 2) AS avg_completed_fare 
FROM trips 
GROUP BY start_station 
ORDER BY revenue DESC;

SELECT COUNT(*) AS total_trips, 
       ROUND(SUM(fee_inr),2) AS total_fare 
FROM trips;

SELECT start_station, 
       COUNT(*) AS departures 
FROM trips 
GROUP BY start_station 
HAVING COUNT(*) >= 67 
ORDER BY departures DESC, start_station;

SELECT start_station, 
       SUM(status = 'cancelled') AS cancelled, 
       ROUND(100 * SUM(status = 'cancelled') / COUNT(*), 1) AS cancel_pct 
FROM trips 
GROUP BY start_station 
ORDER BY cancel_pct DESC, start_station;

SELECT ROUND(AVG(fee_inr),2) AS avg_all_rows, 
       (SELECT ROUND(AVG(fee_inr),2) FROM trips WHERE status = 'completed') AS avg_completed 
FROM trips 
LIMIT 1;