-- list all the cities of California that can be found in the database
-- TASK 8
USE hbtn_0d_usa;

SELECT id, name FROM cities WHERE state_id = 1 ORDER BY id ASC