import csv
import re
import os

# Prompt the user to enter data in a form
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email address: ")
password = input("Enter your password: ")

# Validate the user input
if not name or not age or not email or not password:
    print("\033[91mError: All fields are required\033[0m")
    exit()

try:
    age = int(age)
except ValueError:
    print("\033[38;5;220mError: Age must be a number\033[0m")
    exit()

if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("\033[91mError: Email address is not valid\033[0m")
    exit()

if len(password) < 8:
    print("\033[91mError: Password must be at least 8 characters long\033[0m")
    exit()

# Write the data to a CSV file
with open('formvalidation.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([name, age, email, password])
    print("\033[92mSuccess: Data is Verified\033[0m")

# Run login.py
os.system('python login.py')
