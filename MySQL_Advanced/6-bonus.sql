-- creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;
    INSERT INTO bonuses (user_id, project_id, score)
    VALUES (user_id, project_id, score);
    UPDATE students
    SET average_score = (
        SELECT AVG(score)
        FROM bonuses
        WHERE user_id = user_id
    )
    WHERE id = user_id;
END //
DELIMITER ;
