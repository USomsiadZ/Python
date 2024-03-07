import mysql.connector
from tabulate import tabulate











mydb = mysql.connector.connect(
  host="localhost",
  user="Admin",
  password="toor",
  database="mydatabase"
)
mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()


print(tabulate(myresult, headers=['EmpName', 'EmpSalary'], tablefmt='psql'))