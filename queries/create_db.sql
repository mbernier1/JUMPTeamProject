-- Active: 1675888900621@@127.0.0.1@3306@pokemon_db
DROP DATABASE IF EXISTS pokemon_db;
CREATE DATABASE pokemon_db;
USE pokemon_db;

DROP TABLE IF EXISTS cards;
CREATE TABLE cards (
    card_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    card_name VARCHAR(40) NOT NULL,
    stage SMALLINT NOT NULL,
    retreat_cost SMALLINT,
    hp INT NOT NULL,
    price FLOAT NOT NULL
);

DROP TABLE IF EXISTS users;
CREATE TABLE users(
    user_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL,
    userpassword VARCHAR(40) NOT NULL
);

DROP TABLE IF EXISTS types;
CREATE TABLE types(
    type_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(40) NOT NULL
);

DROP TABLE IF EXISTS sales;
CREATE TABLE sales(
    sale_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    user_id INT UNSIGNED,
    date DATE,
    CONSTRAINT fk_sale_user FOREIGN KEY(user_id) REFERENCES users(user_id)
);

DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews(
    review_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    user_id INT UNSIGNED NOT NULL,
    card_id INT UNSIGNED NOT NULL,
    rating SMALLINT NOT NULL,
    review VARCHAR(255),
    CONSTRAINT fk_review_user FOREIGN KEY (user_id) REFERENCES users(user_id),
    CONSTRAINT fk_review_card FOREIGN KEY (card_id) REFERENCES cards(card_id)
);

DROP TABLE IF EXISTS cards_types;
CREATE TABLE cards_types(
    card_id INT UNSIGNED NOT NULL,
    type_id INT UNSIGNED NOT NULL,
    CONSTRAINT fk_card FOREIGN KEY (card_id) REFERENCES cards(card_id),
    CONSTRAINT fk_type FOREIGN KEY (type_id) REFERENCES types(type_id)
);

DROP TABLE IF EXISTS cards_sales;
CREATE TABLE cards_sales(
    card_id INT UNSIGNED NOT NULL,
    sale_id INT UNSIGNED NOT NULL,
    CONSTRAINT fk_card_sale FOREIGN KEY (card_id) REFERENCES cards(card_id),
    CONSTRAINT fk_sale FOREIGN KEY (sale_id) REFERENCES sales(sale_id)
);


DROP TABLE IF EXISTS user_inv;
CREATE TABLE user_inv(
    user_id INT UNSIGNED NOT NULL,
    card_id INT UNSIGNED NOT NULL,
    quantity INT UNSIGNED NOT NULL,
    CONSTRAINT fk_user_inv FOREIGN KEY (user_id) REFERENCES users(user_id),
    CONSTRAINT fk_card_inv FOREIGN KEY (card_id) REFERENCES cards(card_id)
);

CREATE TABLE sessions(
    session_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    user_id INT UNSIGNED NOT NULL,
    CONSTRAINT fk_session_user FOREIGN KEY (user_id) REFERENCES users(user_id)
);