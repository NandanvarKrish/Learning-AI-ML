USE bike_analytics;

-- Phase 1: Top 10 by minutes (with tie-breaker)
SELECT trip_id, minutes 
FROM trips 
WHERE status = 'completed' 
ORDER BY minutes DESC, trip_id 
LIMIT 10;

-- Phase 2: Pages with no overlap
-- Page 1
SELECT trip_id, minutes FROM trips WHERE status = 'completed' ORDER BY minutes DESC, trip_id LIMIT 10 OFFSET 0;
-- Page 2
SELECT trip_id, minutes FROM trips WHERE status = 'completed' ORDER BY minutes DESC, trip_id LIMIT 10 OFFSET 10;
-- Distinct check (Proves no overlap in the top 20)
SELECT COUNT(DISTINCT trip_id) AS distinct_ids 
FROM (
    SELECT trip_id FROM trips WHERE status = 'completed' ORDER BY minutes DESC, trip_id LIMIT 20
) t;

-- Phase 3: Cheapest real fee (Guarding against NULL)
SELECT trip_id, fee_inr 
FROM trips 
WHERE status = 'completed' AND bike_type = 'electric' AND fee_inr IS NOT NULL 
ORDER BY fee_inr, trip_id 
LIMIT 1;

-- Phase 4: Monday top 20 and the cutoff
-- The Top 20 list
SELECT trip_id, minutes FROM trips WHERE status = 'completed' ORDER BY minutes DESC, trip_id LIMIT 20;
-- Count how many rides are tied at the 20th place cutoff
SELECT COUNT(*) AS tied_at_cutoff 
FROM trips 
WHERE status = 'completed' 
  AND minutes = (
      SELECT minutes FROM trips WHERE status = 'completed' ORDER BY minutes DESC, trip_id LIMIT 1 OFFSET 19
  );

-- Phase 5: Five most recent trips
SELECT trip_id, started_at 
FROM trips 
ORDER BY started_at DESC, trip_id DESC 
LIMIT 5;