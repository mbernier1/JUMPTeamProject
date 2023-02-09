select sales.sale_id, cards.card_id, cards.price, sales.date
from sales
join users on users.user_id = sales.user_id
join cards_sales on cards_sales.sale_id = sales.sale_id
join cards on cards.card_id = cards_sales.card_id
where users.user_id = %s;