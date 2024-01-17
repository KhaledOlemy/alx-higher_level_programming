-- creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (
id int,
name varchar(256),
score int
);
INSERT INTO second_table values(1, "John", 10);
INSERT INTO second_table values(2, "Alex", 3);
INSERT INTO second_table values(3, "Bob", 14);
INSERT INTO second_table values(4, "George", 8);
