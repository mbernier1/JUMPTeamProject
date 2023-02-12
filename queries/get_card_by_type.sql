-- Active: 1675888900621@@127.0.0.1@3306@pokemon_db
SELECT *
FROM cards
JOIN cards_types ct
    ON cards.card_id = ct.card_id
JOIN types
    ON ct.type_id = types.type_id
WHERE types.type_name LIKE CONCAT(%s, '%');