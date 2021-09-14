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
    password= USER_PASSWORD,
    database ='insert_database_name',
    port = 3306
    )

print("I might be connected")

# Cursor
cur = con.cursor()
# Executes the cursor.
cur.execute("SELECT * FROM user")
userRows = cur.fetchall()
# Prints each row of each user.
for eachrow in userRows:
    print(f" {eachrow[0]} {eachrow[1]} {eachrow[2]} ")


cur.execute("SELECT item1 FROM userItem")
userItem = cur.fetchall()
# Prints each mock item for item1 from stored in database
for eachrow in userItem:
    print(f" {eachrow[0]}")


# Close cursor
cur.close()  
# Close connection
con.close()
