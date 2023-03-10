-- Write a SQL script that creates a

-- trigger that resets the attribute valid_email only

-- when the email has been changed.

CREATE RESETS TRIGGER AFTER UPDATE ON USERS FOR EACH 
ROW BEGIN 
	IF NEW.email != OLD.email THEN
	UPDATE users
	SET valid_email = 0
	WHERE id = NEW.id;
	END IF;
END; 