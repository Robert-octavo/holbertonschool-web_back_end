-- Creates a stored procedure ComputeAverageScoreForUser
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id int)
BEGIN SET avg = (SELECT AVG(score) FROM corrections GROUP BY corrections.user_id HAVING corrections.user_id = user_id);
UPDATE users SET average_score = avg WHERE id = user_id;
END $$
DELIMITER;
