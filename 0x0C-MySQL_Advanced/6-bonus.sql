-- SQL script that creates a stored procedure

DELIMITER $$

CREATE PROCEDURE ADDBONUS(USER_ID INT, PROJECT_NAME 
VARCHAR(255), SCORE INT) BEGIN 
	SET @project_id = (
	        SELECT id
	        FROM projects
	        WHERE
	            name = project_name
	    );
	IF @project_id IS NULL THEN
	INSERT INTO projects(name)
	VALUES (project_name);
	SET @project_id = (
	        SELECT id
	        FROM projects
	        WHERE
	            name = project_name
	    );
	END IF;
	INSERT INTO
	    corrections(user_id, project_id, score)
	VALUES (user_id, @project_id, score);
	END 
$ 

$ 

DELIMITER;