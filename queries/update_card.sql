SELECT * FROM cards
UPDATE cards
SET card_name = %s, stage = %s, retreat_cost = %s, hp = %s, price = %s
WHERE card_name =
