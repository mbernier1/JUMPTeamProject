-- Select all reviews for a card
SELECT
    u.username,
    c.card_name,
    rating,
    review
FROM reviews AS r
INNER JOIN cards AS c
    ON c.card_id = r.card_id
INNER JOIN users AS u
    on u.user_id = r.user_id
WHERE c.card_name = %s;