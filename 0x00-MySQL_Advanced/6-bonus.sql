-- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

-- Requirements:

-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- score, the score value for the correction
-- Context: Write code in SQL is a nice level up!

// DELIMITER

CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;
    DECLARE user_project_id INT;

    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;

    IF project_id IS NULL THEN
        INSERT INTO projects (name)
        VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    SELECT id INTO user_project_id
    FROM users_projects
    WHERE user_id = user_id AND project_id = project_id;

    IF user_project_id IS NULL THEN
        INSERT INTO users_projects (user_id, project_id, score)
        VALUES (user_id, project_id, score);
    ELSE
        UPDATE users_projects
        SET score = score + score
        WHERE user_id = user_id AND project_id = project_id;
    END IF;
END;

//
DELIMITER
