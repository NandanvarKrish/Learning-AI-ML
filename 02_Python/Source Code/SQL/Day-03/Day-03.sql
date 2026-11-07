SELECT trip_id, fee_inr FROM trips WHERE status = 'completed' ORDER BY fee_inr DESC, trip_id LIMIT 5;

SELECT trip_id, fee_inr AS fee FROM trips WHERE status = 'completed' ORDER BY fee DESC, trip_id LIMIT 3;

SELECT COUNT(*) AS trips_sharing_a_start_time FROM (SELECT started_at FROM trips GROUP BY started_at HAVING COUNT(*) > 1) t;

SELECT trip_id, minutes FROM trips WHERE status = 'completed' ORDER BY minutes DESC, trip_id LIMIT 20;

SELECT trip_id, started_at FROM trips ORDER BY started_at, trip_id LIMIT 10 OFFSET 10;

SELECT trip_id, started_at FROM trips ORDER BY started_at DESC, trip_id DESC LIMIT 3;

SELECT x FROM (SELECT NULL AS x UNION ALL SELECT 1 UNION ALL SELECT 2) t ORDER BY x;

SELECT trip_id, fee_inr FROM trips WHERE status = 'completed' AND bike_type = 'electric' AND fee_inr IS NOT NULL ORDER BY fee_inr, trip_id LIMIT 1;

SELECT x FROM (SELECT '9' AS x UNION ALL SELECT '10' UNION ALL SELECT '100') t ORDER BY x;

SELECT trip_id, minutes FROM trips WHERE status = 'completed' ORDER BY minutes DESC, trip_id LIMIT 20;

SELECT trip_id, fee_inr FROM trips WHERE status = 'completed' AND bike_type = 'electric' AND fee_inr IS NOT NULL ORDER BY fee_inr, trip_id LIMIT 1;

SELECT trip_id, started_at, minutes FROM trips ORDER BY started_at DESC, trip_id DESC LIMIT 5;

SELECT trip_id, started_at FROM trips ORDER BY started_at, trip_id LIMIT 10 OFFSET 20;