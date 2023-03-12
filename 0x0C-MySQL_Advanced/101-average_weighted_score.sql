-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the

-- average wieihgted score for all students

-- take no input

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers
() BEGIN 
	DECLARE avg_score FLOAT;
	SELECT
	    SUM(score * weight) / SUM(weight) INTO avg_score
	FROM users AS u
	    JOIN corrections as c ON u.id = c.user_id
	    JOIN projects AS p ON c.project_id = p.id
	UPDATE users SET average_score = avg_score 
END$$ 

DELIMITER;