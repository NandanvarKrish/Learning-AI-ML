SELECT trip_id, minutes, fee_inr FROM trips WHERE status = 'completed' AND minutes > 60 ORDER BY trip_id LIMIT 8;

SELECT COUNT(*) AS cancelled_or_zero_fee FROM trips WHERE status = 'cancelled' OR fee_inr = 0;

SELECT COUNT(*) AS no_parentheses FROM trips WHERE bike_type = 'electric' AND status = 'cancelled' OR bike_type = 'classic';

SELECT COUNT(*) AS with_parentheses FROM trips WHERE bike_type = 'electric' AND (status = 'cancelled' OR bike_type = 'classic');

SELECT COUNT(*) AS not_completed FROM trips WHERE NOT (status = 'completed');

SELECT COUNT(*) AS wrong_end, (SELECT COUNT(*) FROM trips WHERE started_at BETWEEN '2026-08-01' AND '2026-08-31 23:59:59') AS right_end FROM trips WHERE started_at BETWEEN '2026-08-01' AND '2026-08-31';

SELECT COUNT(*) AS mid_fare FROM trips WHERE status = 'completed' AND fee_inr BETWEEN 100 AND 200;

SELECT name, zone FROM stations WHERE zone IN ('Core', 'Campus') ORDER BY name;

SELECT name FROM stations WHERE name LIKE '_TADIUM' OR name LIKE 'H%' ORDER BY name;

SELECT name FROM stations WHERE name LIKE '%SIDE%';

SELECT NULL = NULL AS equals_test, NULL IS NULL AS is_null_test;

SELECT COUNT(*) AS missing_end_station FROM trips WHERE end_station IS NULL;

SELECT COUNT(*) AS upper_case_search FROM trips WHERE status = 'COMPLETED';

SELECT COUNT(*) AS electric_cancelled FROM trips WHERE bike_type = 'electric' AND status = 'cancelled';

SELECT COUNT(*) AS mid_band_rides FROM trips WHERE status = 'completed' AND fee_inr BETWEEN 100 AND 200;

SELECT COUNT(*) AS sept_waterfront_departures FROM trips WHERE start_station IN ('HARBOUR', 'RIVERSIDE') AND started_at BETWEEN '2026-09-01' AND '2026-09-30 23:59:59';

SELECT COUNT(*) AS completed_zero_minutes FROM trips WHERE status = 'completed' AND minutes = 0;