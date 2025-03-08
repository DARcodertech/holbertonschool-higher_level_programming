-- list a citie 
SELECT id, name
FROM FROM hbtn_0d_usa.cities
WHERE state_id = (
    SELECT id
    FROM hbtn_0d_usa.states
    WHERE name = 'California'
)
ORDER BY id ASC;
