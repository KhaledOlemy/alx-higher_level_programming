-- creates the database hbtn_0d_usa and the table cities (in the database \
-- hbtn_0d_usa) on your MySQL server.
-- cities: id INT primary key, auto generated.
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to\
-- id of the states table, name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
id INT PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id));
