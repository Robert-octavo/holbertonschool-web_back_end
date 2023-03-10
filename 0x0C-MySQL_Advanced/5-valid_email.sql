-- Write a SQL script that creates a TRIGGER
DELIMITER $$
CREATE TRIGGER resets BEFORE UPDATE ON users FOR EACH 
ROW BEGIN 
	IF NEW.email <> OLD.email THEN
		SET NEW.valid_email = 0
	END IF;
END;
$$
DELIMITER;
