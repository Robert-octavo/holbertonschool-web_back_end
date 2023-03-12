-- creates a store procedure ComputeAverageWeightedScoreForUser

-- that computes and store the average wieghted score for a student

-- take one input

-- user_id value ADD

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser
(IN user_id INT) BEGIN 
	DECLARE avg_score FLOAT;
	SELECT
	    SUM(score*weight) / SUM(weight) INTO avg_score
	FROM AS u JOIN corrections as c ON u.id=c.user_id
	JOIN projects AS p ON c.project_id=p.id
	WHERE id = user_id;
	UPDATE users
	SET
	    average_score = avg_score
	WHERE id = user_id;
END$$ 

DELIMITER;
