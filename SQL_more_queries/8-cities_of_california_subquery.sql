-- list a citie 
SELECT cities.id, cities.name
FROM hbtn_0d_usa.cities AS cities
WHERE cities.state_id = (
    SELECT states.id
    FROM hbtn_0d_usa.states AS states
    WHERE states.name = 'California'
)
ORDER BY cities.id ASC;
