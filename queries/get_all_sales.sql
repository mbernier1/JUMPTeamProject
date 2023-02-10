SELECT DISTINCT sales.sale_id, sales.date
FROM sales
JOIN cards_sales ON cards_sales.sale_id = sales.sale_id
JOIN cards ON cards.card_id = cards_sales.card_id
ORDER BY sales.sale_id;