UPDATE user_inv
SET quantity = quantity + 1
WHERE card_id = %s;