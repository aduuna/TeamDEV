DROP TABLE freelancer CASCADE;
DROP TABLE employer CASCADE;
DROP TABLE job_postings CASCADE;
DROP TABLE comment CASCADE;
DROP TABLE job_allocation CASCADE;

CREATE TABLE freelancer (
  freelancer_id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  dateofbirth DATE NOT NULL,
  status VARCHAR(255) NOT NULL,
  skills VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,	
  email VARCHAR(255) NOT NULL,
  contact VARCHAR(255) NOT NULL);

CREATE TABLE employer (
   employer_id SERIAL PRIMARY KEY,
   company_name VARCHAR(255) NOT NULL,
   company_description VARCHAR(255) NOT NULL,
   email VARCHAR(255) NOT NULL,
   contact VARCHAR(255) NOT NULL);

CREATE TABLE job_postings (
  job_id SERIAL PRIMARY KEY,
  employer_id INTEGER NOT NULL,
  title VARCHAR(255) NOT NULL,
  description VARCHAR(255) NOT NULL,
  duration VARCHAR(255) NOT NULL,
  no_of_people INTEGER NOT NULL,
  FOREIGN KEY (employer_id)
  REFERENCES employer (employer_id)
  ON UPDATE CASCADE ON DELETE CASCADE,
  amount REAL NOT NULL);


CREATE TABLE comment (
  comment_id SERIAL PRIMARY KEY,
  employer_id INTEGER NOT NULL,
  freelancer_id INTEGER NOT NULL,
  FOREIGN KEY (employer_id)
  REFERENCES employer (employer_id)
  ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (freelancer_id)
        REFERENCES freelancer (freelancer_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
        comment VARCHAR(255) NOT NULL,
        dateofcomment DATE NOT NULL,
        timeofcomment TIME NOT NULL,
        rating INTEGER NOT NULL);

CREATE TABLE job_allocation (
      freelancer_id INTEGER NOT NULL,
      job_id INTEGER NOT NULL,
      FOREIGN KEY (freelancer_id)
      REFERENCES freelancer (freelancer_id)
      ON UPDATE CASCADE ON DELETE CASCADE,
      FOREIGN KEY (job_id)
      REFERENCES job_postings (job_id)
      ON UPDATE CASCADE ON DELETE CASCADE);

INSERT INTO freelancer(first_name, last_name, dateofbirth, status, skills, password, email, contact) 
VALUES ('Doreen', 'Dodoo', '1996-05-03', 'unemployed', 'none', '123456', 'dummy@dummyemail.com', '0244879058' );
