USE bike_analytics;

-- Phase 1: Partition check
SELECT COUNT(*) AS total FROM trips;
SELECT COUNT(*) AS completed FROM trips WHERE status = 'completed';
SELECT COUNT(*) AS cancelled FROM trips WHERE status = 'cancelled';

-- Phase 2: Cancellation rate by bike type
SELECT COUNT(*) AS electric_cancelled FROM trips WHERE bike_type = 'electric' AND status = 'cancelled';
SELECT COUNT(*) AS classic_cancelled FROM trips WHERE bike_type = 'classic' AND status = 'cancelled';
SELECT COUNT(*) AS electric_total FROM trips WHERE bike_type = 'electric';
SELECT COUNT(*) AS classic_total FROM trips WHERE bike_type = 'classic';

-- Phase 3: Date window with the right boundary
-- Correct boundary (includes the whole last day)
SELECT COUNT(*) AS aug FROM trips WHERE started_at BETWEEN '2026-08-01' AND '2026-08-31 23:59:59';
-- Wrong boundary (drops trips after midnight on the 31st)
SELECT COUNT(*) AS aug_wrong FROM trips WHERE started_at BETWEEN '2026-08-01' AND '2026-08-31';

-- Phase 4: Parentheses and the owner's question
-- Correct logic
SELECT COUNT(*) AS with_parens FROM trips WHERE bike_type = 'electric' AND (status = 'cancelled' OR fee_inr = 0);
-- Precedence trap (evaluates AND before OR)
SELECT COUNT(*) AS without_parens FROM trips WHERE bike_type = 'electric' AND status = 'cancelled' OR fee_inr = 0;

-- Phase 5: Data-quality rules (All should return 0)
SELECT 
  (SELECT COUNT(*) FROM trips WHERE status = 'completed' AND minutes = 0) AS zero_minutes,
  (SELECT COUNT(*) FROM trips WHERE status = 'cancelled' AND fee_inr > 0) AS cancelled_with_fee,
  (SELECT COUNT(*) FROM trips WHERE minutes < 0) AS negative_minutes;