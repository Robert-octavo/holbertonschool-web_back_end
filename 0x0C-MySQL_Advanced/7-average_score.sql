-- Create a procedure

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN USER_ID 
INT) BEGIN 
	UPDATE users
	SET average = (
	        SELECT AVG(score)
	        FROM corrections
	        WHERE user_id = USER_ID
	    )
	WHERE id = USER_ID;
END$ 

$ 

DELIMITER ;