-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the

-- average wieihgted score for all students

-- take no input

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers() 
	BEGIN 
	UPDATE users AS u,
	(SELECT
	    SUM(score * weight) / SUM(weight) AS avg_score
	FROM users AS u
	    JOIN corrections as c ON u.id = c.user_id
	    JOIN projects AS p ON c.project_id = p.id
	GROUP BY u.id) AS uavg_score
	SET u.average_score = uavg_score.avg_score
	WHERE u.id=uavg_score.id 
END$$ 

DELIMITER;