USE bike_analytics;

SELECT COUNT(*) AS trips, COUNT(DISTINCT start_station) AS stations, ROUND(SUM(fee_inr),2) AS revenue, ROUND(AVG(minutes),1) AS avg_minutes FROM trips WHERE status = 'completed';

SELECT start_station, COUNT(*) AS departures, ROUND(SUM(fee_inr),2) AS revenue FROM trips GROUP BY start_station ORDER BY revenue DESC;

SELECT bike_type, COUNT(*) AS trips, ROUND(AVG(minutes),1) AS avg_minutes FROM trips WHERE status = 'completed' GROUP BY bike_type ORDER BY bike_type;

SELECT start_station, COUNT(*) AS departures FROM trips GROUP BY start_station HAVING COUNT(*) >= 67 ORDER BY departures DESC, start_station;

SELECT start_station, COUNT(*) AS completed_trips FROM trips WHERE status = 'completed' GROUP BY start_station HAVING COUNT(*) >= 60 ORDER BY completed_trips DESC, start_station;

SELECT COUNT(*) AS all_rows, COUNT(end_station) AS with_end_station, COUNT(DISTINCT start_station) AS distinct_start_stations FROM trips;

SELECT status, COUNT(*) AS trips, ROUND(SUM(fee_inr),2) AS fares, ROUND(AVG(fee_inr),2) AS avg_fee FROM trips GROUP BY status ORDER BY status;

SELECT bike_type, COUNT(*) AS cancelled FROM trips WHERE status = 'cancelled' GROUP BY bike_type ORDER BY bike_type;

SELECT start_station, COUNT(*) AS departures, ROUND(SUM(fee_inr),2) AS revenue, ROUND(SUM(fee_inr) / SUM(status = 'completed'), 2) AS avg_completed_fare FROM trips GROUP BY start_station ORDER BY revenue DESC;

SELECT bike_id, COUNT(*) AS trips FROM trips GROUP BY bike_id HAVING COUNT(*) > 33 ORDER BY trips DESC, bike_id;

SELECT status, COUNT(*) AS trips, ROUND(SUM(fee_inr),2) AS fares FROM trips GROUP BY status ORDER BY status;

