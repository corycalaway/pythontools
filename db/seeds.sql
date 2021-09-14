USE insert_database_name;

INSERT INTO userItem
    (item1)
VALUES
    ('Mock Item 1'),
    ('Mock Item 2'),
    ('Mock Item 3'),
    ('Mock Item 4');

INSERT INTO user 
    (username, user_item_id, user_rating)
VALUES 
    ('User 1', 3, 4),
    ('User 2', 1, 3),
    ('User 3', 4, 2),
    ('User 4', 2, 10);