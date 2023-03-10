-- Create a procedure

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT) 
BEGIN 	SET avg = (SELECT AVG(score) FROM corrections GROUP BY corrections.user_id HAVING corrections.user_id = user_id)
	UPDATE users
	SET average = avg
	WHERE id = user_id;
END;$$ 

DELIMITER ;