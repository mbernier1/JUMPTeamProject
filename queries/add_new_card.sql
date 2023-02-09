SELECT * FROM cards
INSERT INTO cards (card_name, stage, retreat_cost, hp, price) 
VALUES (card_name, %s, %s, %s, %s)