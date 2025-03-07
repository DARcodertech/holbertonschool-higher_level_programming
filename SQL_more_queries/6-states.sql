-- make a table and database if it dont exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (
    id INT,
    name VARCHAR(256),
    PRIMARY KEY (id)
)