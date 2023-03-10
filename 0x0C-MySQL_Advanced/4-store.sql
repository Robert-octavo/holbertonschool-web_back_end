-- Write a SQL script that creates a trigger that

--decreases the quantity of an item after adding

--a new order.Quantity in the table items can be negative.

DELIMITER $$

DROP TRIGGER
    IF EXISTS decreases $$ CREATE DECREASES TRIGGER AFTER
INSERT
    ON ORDERS FOR EACH ROW BEGIN
UPDATE items
SET
    quantity = quantity - NEW.number
WHERE name = NEW.item_name;

END;

END$$ 

DELIMITER ;