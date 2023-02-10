SELECT cards.card_id, cards.card_name, round(AVG(reviews.rating), 2) as avg_rating 
FROM cards
join reviews
    on cards.card_id = reviews.card_id
GROUP BY cards.card_id
ORDER BY avg_rating DESC