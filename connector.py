import mysql.connector as conn

connection = conn.connect(user='root', password='', host='127.0.0.1', database='recommender_system')

cursor = connection.cursor()

query = "SELECT user_name,password_md5 from user"

cursor.execute(query)

for i in cursor:
    print(i)

cursor.close()
connection.close()