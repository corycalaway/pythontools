DROP DATABASE IF EXISTS insert_database_name;

CREATE DATABASE insert_database_name;

USE insert_database_name;

CREATE TABLE userItem (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    item1 VARCHAR(30) NOT NULL
);

CREATE TABLE user (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(30) UNIQUE NOT NULL,
  user_item_id INT UNSIGNED NOT NULL,
  INDEX idx_user_item (user_item_id),
  CONSTRAINT fk_user_item FOREIGN KEY (user_item_id) REFERENCES userItem(id) ON DELETE CASCADE,
  user_rating INT 
);

