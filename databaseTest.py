import mysql.connector

conn = mysql.connector.connect(username='root', password='SQLconnect@123',host='localhost',database='face_recognition',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data) 

conn.close()
# import mysql.connector

# try:
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="SQLconnect@123",
#         database="face_recognition"
        
#     )
#     print("Connection successful!")
# except mysql.connector.Error as error:
#     print("Error connecting to MySQL: {}".format(error))
