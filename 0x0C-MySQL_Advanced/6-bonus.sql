-- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

-- Procedure AddBonus is taking 3 inputs (in this order):

-- user_id, a users.id value (you can assume user_id is linked to an existing users)

-- project_name, a new or already exists projects - if no projects.name found in the

-- table you should create it

-- score, the score value for the correction

CREATE PROCEDURE AddBonus(IN USER_ID INT, IN PROJECT_NAME 
VARCHAR(255), IN SCORE INT) BEGIN 
	DECLARE project_id INT;
	DECLARE correction_id INT;
	SELECT id INTO project_id
	FROM projects
	WHERE name = project_name;
	IF project_id IS NULL THEN
	INSERT INTO
	    projects (name)
	VALUES (project_name);
	SELECT
	    id INTO project_id
	FROM projects
	WHERE name = project_name;
	END IF;
	INSERT INTO
	    corrections (user_id, project_id, score)
	VALUES (user_id, project_id, score);
	SELECT id INTO correction_id
	FROM corrections
	WHERE
	    user_id = user_id
	    AND project_id = project_id
	    AND score = score;
	INSERT INTO bonuses (correction_id) VALUES (correction_id);
	END 
