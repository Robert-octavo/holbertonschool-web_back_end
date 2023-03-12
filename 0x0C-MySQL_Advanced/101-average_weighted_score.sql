-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the

-- average wieihgted score for all students

-- take no input

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers() 
	BEGIN 
	(SELECT
	    SUM(score * weight) / SUM(weight) AS avg_score
	FROM users AS u
	    JOIN corrections as c ON u.id = c.user_id
	    JOIN projects AS p ON c.project_id = p.id
	GROUP BY u.id) AS uavg_score
	UPDATE users SET average_score = uavg_score.avg_score
	WHERE id=uavg_score.id 
END$$ 

DELIMITER;