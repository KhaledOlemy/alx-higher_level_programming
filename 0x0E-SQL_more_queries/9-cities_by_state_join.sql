-- lists all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- sorted in ascending order by cities.id/one SELECT statement
SELECT c.id, c.name, s.name FROM cities c NATURAL JOIN states s ON (c.state_id = s.id) ORDER BY c.id ASC;
