-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

-- Requirements:

-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE average_score DECIMAL(5, 2);
    
    SELECT AVG(score) INTO average_score
    FROM users_projects
    WHERE user_id = user_id;
    
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END;
