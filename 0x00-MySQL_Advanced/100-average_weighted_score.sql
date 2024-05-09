-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

-- Requirements:

-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE average_weighted_score DECIMAL(5, 2);
    
    SELECT AVG(score * weight) INTO average_weighted_score
    FROM users_projects
    JOIN projects
    ON users_projects.project_id = projects.id
    WHERE user_id = user_id;
    
    UPDATE users
    SET average_weighted_score = average_weighted_score
    WHERE id = user_id;
END;
