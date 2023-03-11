-- Creates a function SafeDiv that divides (and RETURNS) the first by the second argument

-- or returns 0 if the second argument is 0

-- takes 2 arguments a, int - b, int

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS DOUBLE DETERMINISTIC BEGIN 
	DECLARE result FLOAT;
	IF b = 0 THEN SET result = 0;
	ELSE SET result = a / b;
	END IF;
	RETURN result;
END $$
DELIMITER;