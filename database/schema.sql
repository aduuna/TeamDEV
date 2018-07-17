CREATE TABLE IF NOT EXISTS freelancer (
  freelancer_id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  dateofbirth DATE NOT NULL,
  status VARCHAR(255) NOT NULL,
  skills VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  contact VARCHAR(255) NOT NULL);
