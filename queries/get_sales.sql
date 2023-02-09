SELECT
    s.sale_id,
    s.user_id,
    s.`date`,
    cs.card_id,
    cards.card_name
FROM sales s
JOIN cards_sales cs
    ON s.sale_id = cs.sale_id
JOIN cards
    ON cs.card_id = cards.card_id;