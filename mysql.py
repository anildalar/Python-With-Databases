import mysql.connector

#1. DB Connection Open
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_db"
)

# Set the DB Cursor

mycursor = mydb.cursor()

# How we can recieve the data from user

name = input("Please Enter your name ?")
contact = input("Please Enter your contact ?")
address = input("Please Enter your address ?")

print(name)
print(contact)
print(address)

#2 Build the query
sql = "INSERT INTO student_tbl (stu_name, stu_contact, stu_addr) VALUES (%s, %s, %s)"
val = (name, contact,address )

#3. Execute the query
mycursor.execute(sql, val)

#
mydb.commit()

#4. Display the result
print(mycursor.rowcount, "Users inserted.")

# To store these information into database student_tbl