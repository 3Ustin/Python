INSERT INTO users (first_name,last_name,email,created_at,updated_at)
VALUES('Aster', 'Michelsen', 'ASter@Star.net', '2010-02-01 00:00:01','2011-07-01 00:00:01');
INSERT INTO users (first_name,last_name,email,created_at,updated_at)
VALUES('Noah', 'Stenkinson', 'NoStenkinson@University.edu', '2010-02-01 00:00:01','2011-07-01 00:00:01');
INSERT INTO users (first_name,last_name,email,created_at,updated_at)
VALUES('Preston', 'Micha', 'Christian@Trey.Kelvin', '2010-02-01 00:00:01','2011-07-01 00:00:01');
DELETE FROM users LIMIT 3;

UPDATE users SET first_name = 'some_value', last_name ='another_value', email = 'thisEmail@rem', created_at = '2010-02-01 00:00:01', updated_at = '2011-07-01 00:00:01' WHERE id = 56;

SELECT id FROM users WHERE id = 49;
SELECT email FROM users WHERE email = 'Christian@Trey.Kelvin';
SELECT * FROM users_schema.users;

SELECT first_name FROM users ORDER BY first_name DESC;
