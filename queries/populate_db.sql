USE pokemon_db;

INSERT INTO cards VALUES(
    (1, 'Tepig', 0, 2, 70, 3.31),
    (2, 'Victini', 0, 1, 60, 4.85),
    (3, 'Ninetales', 1, 1, 90, 8.35),
    (4, "Snivy", 0, 1, 60, 1.90),
    (5, "Pansage", 0, 1, 60, 1.27),
    (6, "Serperior", 2, 1, 130, 4.23),
    (7, "Oshawott", 0, 1, 60, 3.58),
    (8, "Empoleon", 2, 2, 140, 5.99),
    (9, "Vaporeon", 1, 2, 110, 4.20),
    (10, "Pikachu", 0, 1, 60, 2.34),
    (11, "Ampharos", 2, 2, 140, 5.11),
    (12, "Electrode", 1, 0, 100, 5.99)
);

INSERT INTO types VALUES(
    (1, "Fire"),
    (2, "Grass"),
    (3, "Water"),
    (4, "Lightning")
);

INSERT INTO cards_types VALUES(
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
    (12, 4)
);