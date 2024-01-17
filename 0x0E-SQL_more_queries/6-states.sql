-- creates the database hbtn_0d_usa and the table states (in the database \
-- hbtn_0d_usa) on your MySQL server.
-- states: id INT PRIMARY KEY, auto generated, name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256));
