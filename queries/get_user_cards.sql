SELECT
    u.user_id,
    u.email,
    c.card_id,
    inv.quantity,
    card_name,
    stage,
    retreat_cost,
    hp,
    price
FROM users u
JOIN user_inv AS inv
    ON u.user_id = inv.user_id
JOIN cards c
    ON inv.card_id = c.card_id
WHERE u.user_id LIKE %s;