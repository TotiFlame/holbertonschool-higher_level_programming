-- list all cities contained in the database
SELECT cities.id, cities.name, states.name FROM states JOIN cities on states.id = cities.states_id ORDER BY ASC;