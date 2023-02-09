USE pokemon_db;

INSERT INTO cards (card_id, card_name, stage, retreat_cost, hp, price) VALUES
    (1, "Tepig", 0, 2, 70, 3.31),
    (2, "Victini", 0, 1, 60, 4.85),
    (3, "Ninetales", 1, 1, 90, 8.35),
    (4, "Snivy", 0, 1, 60, 1.90),
    (5, "Pansage", 0, 1, 60, 1.27),
    (6, "Serperior", 2, 1, 130, 4.23),
    (7, "Oshawott", 0, 1, 60, 3.58),
    (8, "Empoleon", 2, 2, 140, 5.99),
    (9, "Vaporeon", 1, 2, 110, 4.20),
    (10, "Pikachu", 0, 1, 60, 2.34),
    (11, "Ampharos", 2, 2, 140, 5.11),
    (12, "Electrode", 1, 0, 100, 5.99)
;

INSERT INTO types (type_id, type_name) VALUES
    (1, "Fire"),
    (2, "Grass"),
    (3, "Water"),
    (4, "Lightning");

INSERT INTO cards_types (card_id, type_id) VALUES 
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 2),
    (6, 2),
    (7, 3),
    (8, 3),
    (9, 3),
    (10, 4),
    (11, 4),
    (12, 4);

INSERT INTO users (user_id , email, password) VALUES
    (1, "ruperto@gmail.com", "save the princess"),
    (2, "mauricio@outlook.com", "textile engineer"),
    (3, "zieglar@yahoo.com", "margarethe");

INSERT INTO reviews (review_id, user_id, card_id, rating, review) VALUES
    (1, 1, 3, 4, "Absolutely poggers"),
    (2, 2, 7, 3, "It is what it is"),
    (3, 3, 12, 5, "Ich liebe diese Karte");

INSERT INTO sales (sale_id, `date`, user_id) VALUES
    (1, "2018-03-25", 1),
    (2, "2019-11-11", 2),
    (3, "2015-12-25", 3);

INSERT INTO cards_sales (sale_id, card_id) VALUES
    (1, 3),
    (2, 7),
    (3, 12);

INSERT INTO user_inv (user_id, card_id, quantity) VALUES
    (1, 3, 1),
    (1, 8, 5),
    (2, 7, 2),
    (2, 4, 2),
    (3, 12, 3),
    (3, 2, 3);