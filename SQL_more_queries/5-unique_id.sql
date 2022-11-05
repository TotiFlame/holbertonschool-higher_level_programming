-- creates the table unique_id
-- task 5
CREATE TABLE IF NOT EXISTS unique_id (
    id int DEFAULT 1 UNIQUE,
    name varchar (256)
);