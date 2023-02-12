SELECT * 
FROM cards 
WHERE card_name LIKE CONCAT(%s, '%');