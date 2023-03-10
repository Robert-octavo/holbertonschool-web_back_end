-- Write a SQL script that creates a TRIGGER

DELIMITER $$

CREATE TRIGGER RESETS 
BEFORE UPDATE ON users FOR EACH ROW BEGIN IF OLD.email <> NEW.email THEN SET NEW.valid_email = 0; END IF;
END; 
$$ 
DELIMITER;