import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


USER_PROFILE = os.getenv('USER_PROFILE')
USER_PASSWORD = os.getenv('USER_PASSWORD')

# Connecting to a database
con = mysql.connector.connect(
    host = 'localhost',
    user = USER_PROFILE,
    password = USER_PASSWORD,
    database ='insert_database_name',
    port = 3306
    )

print(con)

# Cursor
cur = con.cursor()
# Executes the cursor.
cur.execute("SELECT * FROM user")
userRows = cur.fetchall()
# Prints each row of each user.
for eachrow in userRows:
    print(f" {eachrow[0]} {eachrow[1]} {eachrow[2]} ")

# Query userItem item 1
cur.execute("SELECT item1 FROM userItem")
userItem = cur.fetchall()
# Prints each mock item for item1 from stored in database
for eachrow in userItem:
    print(f" {eachrow[0]}")


add_username = str(input("What username would you like to add? "))

add_user_item = int(input("Please enter the id number of the user item. "))

add_user_rating = int(input("Please enter the users rating from 1 - 5. "))

print(add_username)

# Adds inputs to database
cur.execute(
    'INSERT INTO user (username, user_item_id, user_rating) VALUES ("{}", {}, {})' .format(add_username, add_user_item, add_user_rating))


# Commit connection
con.commit()

user_to_update = str(input("Enter the username of the user to update. "))

new_rating = int(input("What would you like to update {} rating to. " .format(user_to_update)))

# Update selected user by username to update user rating.
cur.execute('UPDATE user SET user_rating = {} WHERE username = "{}";' .format(new_rating, user_to_update))

con.commit()
# Close cursor
cur.close()  
# Close connection
con.close()
