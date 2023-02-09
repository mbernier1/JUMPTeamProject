SELECT
    review_id,
    users.user_id,
    users.username,
    cards.card_id,
    cards.card_name,
    reviews.rating,
    reviews.review
FROM reviews
JOIN cards
    ON cards.card_id = reviews.card_id
JOIN users
    ON reviews.user_id = users.user_id
WHERE cards.card_id = %s;