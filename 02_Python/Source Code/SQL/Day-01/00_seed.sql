-- 00_seed.sql : bike_analytics practice database (re-runnable, deterministic)
CREATE DATABASE IF NOT EXISTS bike_analytics;
USE bike_analytics;
DROP TABLE IF EXISTS trips;
DROP TABLE IF EXISTS stations;

CREATE TABLE stations (
  name   VARCHAR(16) PRIMARY KEY,
  zone   VARCHAR(20) NOT NULL,
  opened DATE NOT NULL
);

CREATE TABLE trips (
  trip_id       INT PRIMARY KEY,
  bike_id       CHAR(3) NOT NULL,
  bike_type     ENUM('classic','electric') NOT NULL,
  start_station VARCHAR(16) NOT NULL,
  end_station   VARCHAR(16) NOT NULL,
  started_at    DATETIME NOT NULL,
  minutes       INT NOT NULL CHECK (minutes >= 0),
  fee_inr       DECIMAL(8,2) NOT NULL CHECK (fee_inr >= 0),
  status        ENUM('completed','cancelled') NOT NULL,
  FOREIGN KEY (start_station) REFERENCES stations(name),
  FOREIGN KEY (end_station)   REFERENCES stations(name)
);

INSERT INTO stations (name, zone, opened) VALUES
  ('CENTRAL','Core','2019-03-01'), ('MARKET','Core','2019-06-15'),
  ('RIVERSIDE','Waterfront','2020-01-10'), ('HARBOUR','Waterfront','2021-05-03'),
  ('UNIVERSITY','Campus','2020-08-20'), ('STADIUM','Sports','2022-02-14');

INSERT INTO trips (trip_id, bike_id, bike_type, start_station, end_station, started_at, minutes, fee_inr, status)
WITH RECURSIVE seq AS (
  SELECT 1 AS n
  UNION ALL
  SELECT n + 1 FROM seq WHERE n < 400
),
calc AS (
  SELECT n,
         1 + MOD(n * 7, 12)            AS bike_no,
         MOD(n * 5, 6)                 AS si,
         MOD(n * 5, 6) + 1 + MOD(n, 5) AS ei_raw,
         3 + MOD(n * 17, 68)           AS mins_raw,
         (MOD(n, 17) = 0)              AS is_cancel,
         TIMESTAMP('2026-07-01') + INTERVAL MOD(n * 37, 120) DAY
           + INTERVAL MOD(n * 13, 24) HOUR + INTERVAL MOD(n * 29, 60) MINUTE AS started
  FROM seq
)
SELECT n,
       CONCAT('B', LPAD(bike_no, 2, '0')),
       IF(bike_no <= 6, 'classic', 'electric'),
       ELT(si + 1, 'CENTRAL','MARKET','RIVERSIDE','HARBOUR','UNIVERSITY','STADIUM'),
       ELT(MOD(si + 1 + MOD(n, 5), 6) + 1, 'CENTRAL','MARKET','RIVERSIDE','HARBOUR','UNIVERSITY','STADIUM'),
       started,
       IF(is_cancel, 0, mins_raw),
       IF(is_cancel, 0.00,
          IF(bike_no <= 6, 10 + 1.5 * mins_raw, 15 + 2 * mins_raw)),
       IF(is_cancel, 'cancelled', 'completed')
FROM calc;
