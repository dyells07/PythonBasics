import sqlite3
import csv

con = sqlite3.connect("connection.db")
cur = con.cursor()

name = input("Enter customer name: ")
address = input("Enter customer address: ")

sql = "INSERT INTO customers (name, address) VALUES (?, ?)"
val = (name, address)

cur.execute(sql, val)

con.commit()

print(cur.rowcount, "record inserted.")

with open('customers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'address'])
    writer.writerow([cur.lastrowid, name, address])

print("Data written to customers.csv")

con.close()