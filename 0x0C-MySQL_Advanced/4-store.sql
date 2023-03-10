-- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.Quantity in the table items can be negative.

CREATE decreases TRIGGER AFTER INSERT ON ORDERS FOR 
EACH ROW BEGIN 
	UPDATE items
	SET
	    quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END; 
