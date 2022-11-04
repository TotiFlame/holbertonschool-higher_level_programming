-- compute the score average of all records in the table second_table
-- task 14

ALTER TABLE second_table
ADD average float;

INSERT INTO second_table (average) SELECT AVG(score) FROM second_table