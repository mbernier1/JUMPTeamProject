SELECT 
    cards.card_id,
    card_name,
    stage,
    retreat_cost,
    hp, 
    types.type_name,
    price
FROM cards
JOIN cards_types
    ON cards.card_id = cards_types.card_id
JOIN types
    ON cards_types.type_id = types.type_id;

SELECT 
    email, 
    password,
    cards.card_id,
    card_name
FROM users
JOIN user_inv
    ON users.user_id = user_inv.user_id
JOIN cards
    ON cards.card_id = user_inv.card_id;