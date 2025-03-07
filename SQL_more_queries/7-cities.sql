-- make a table and database if it dont exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS  hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL FOREIGN KEY,
    name VARCHAR(256) NOT NULL 
)
