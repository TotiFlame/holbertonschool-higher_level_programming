-- list all cities contained in the database
SELECT cities.id, cities.name, states.name FROM states CROSS JOIN cities ORDER BY ASC;