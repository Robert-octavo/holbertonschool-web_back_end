-- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.Quantity in the table items can be negative.

CREATE TRIGGER DECREASES AFTER INSERT ON ORDERS FOR 
EACH ROW BEGIN 
	UPDATE items
	SET
	    quantity = quantity - NEW.number
	WHERE name = item_name;
END; 