SELECT * FROM cards
INSERT INTO cards (card_name, stage, retreat_cost, hp, price) 
VALUES (%s, %s, %s, %s, %s)