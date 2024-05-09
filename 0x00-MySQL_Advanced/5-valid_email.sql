-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

-- Context: Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

DELIMITER //

CREATE TRIGGER resets_valid_email
AFTER UPDATE ON email
BEGIN
    UPDATE users
    SET valid_email = 0
    WHERE email != OLD.email;
END;

//
DELIMITER ;
