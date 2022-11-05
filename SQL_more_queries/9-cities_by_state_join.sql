-- list all cities contained in the database
SELECT cities.id, cities.name, states.name FROM cities JOIN states on states.id = cities.state_id;