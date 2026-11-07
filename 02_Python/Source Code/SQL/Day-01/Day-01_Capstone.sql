-- Phase 2: Answer the ten audit questions
-- Q1: Total trips

USE bike_analytics;

SELECT COUNT(*) AS trips FROM trips;

-- Q2: Unique trip IDs (Should match Q1)
SELECT COUNT(DISTINCT trip_id) AS unique_ids FROM trips;

-- Q3: Bikes in the fleet
SELECT COUNT(DISTINCT bike_id) AS bikes FROM trips;

-- Q4: Total stations
SELECT COUNT(*) AS stations FROM stations;

-- Q5 & Q6: Date coverage
SELECT MIN(started_at) AS first_trip, 
       MAX(started_at) AS last_trip, 
       COUNT(DISTINCT DATE(started_at)) AS days_with_trips 
FROM trips;

-- Q7: Total revenue
SELECT ROUND(SUM(fee_inr), 2) AS revenue_inr FROM trips;

-- Phase 3: Test the owner's claim & find the newest station
SELECT name, opened 
FROM stations 
ORDER BY opened DESC 
LIMIT 1;