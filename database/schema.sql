DROP TABLE freelancer, employer, job_postings, comment, job_allocation;

CREATE TABLE IF NOT EXISTS freelancer (
  freelancer_id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  dateofbirth DATE NOT NULL,
  status VARCHAR(255) NOT NULL,
  skills VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  contact VARCHAR(255) NOT NULL);


 CREATE TABLE IF NOT EXISTS employer (
   employer_id SERIAL PRIMARY KEY,
   company_name VARCHAR(255) NOT NULL,
   company_description VARCHAR(255) NOT NULL,
   email VARCHAR(255) NOT NULL,
   contact VARCHAR(255) NOT NULL);


CREATE TABLE IF NOT EXISTS job_postings (
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


CREATE TABLE IF NOT EXISTS comment (
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
        rating INTEGER NOT NULL
                
        );

CREATE TABLE IF NOT EXISTS job_allocation (
      freelancer_id INTEGER NOT NULL,
      job_id INTEGER NOT NULL,
      FOREIGN KEY (freelancer_id)
      REFERENCES freelancer (freelancer_id)
      ON UPDATE CASCADE ON DELETE CASCADE,
      FOREIGN KEY (job_id)
      REFERENCES job_postings (job_id)
      ON UPDATE CASCADE ON DELETE CASCADE
               
  );

INSERT INTO freelancer(first_name, last_name, dateofbirth, status, skills, password, email, contact) 
VALUES ('Doreen', 'Dodoo', '1996-05-03', 'unemployed', 'none', '123456', '0244879058' );
INSERT INTO employer(company_name, company_description, email, contact)
VALUES ('Tullow', 'oil company', 'tullow@gmail.com', '0578532331')
INSERT INTO job_postings(employer_id, title, description, duration, no_of_people)
VALUES (2, 'construction work', '2 weeks', 20)
INSERT INTO comment(employer_id, freelancer_id, comment, dateofcomment, timeofcomment, rating)
VALUES (5, 1, 'Very hardworking', '1971-07-13', '01:00:00', 5)
INSERT INTO job_allocation(freelancer_id, job_id)
VALUES (2, 5)
