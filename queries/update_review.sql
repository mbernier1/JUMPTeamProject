UPDATE reviews
SET email = %s, cardname = %s, rating = %s, review = %s
WHERE rating_id = %s;