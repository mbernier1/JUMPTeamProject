select sales.sale_id, sales.date, cards.card_name, price
from sales
join cards_sales on cards_sales.sale_id=sales.sale_id
join cards on cards.card_id = cards_sales.card_id
where sales.sale_id = %s;