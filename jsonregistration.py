import json
import re
import os
from termcolor import colored

# Print the header
print(colored("=" * 40, "magenta"))
print(colored(" " * 15 + "REGISTER" + " " * 15, "white", "on_magenta", attrs=["bold"]))
print(colored("=" * 40, "magenta"))

# Prompt the user to enter data in a form
name = input(colored("Enter your name: ", "yellow"))
age = input(colored("Enter your age: ", "yellow"))
email = input(colored("Enter your email address: ", "yellow"))
password = input(colored("Enter your password: ", "yellow"))

# Validate the user input
if not name or not age or not email or not password:
    print(colored("Error: All fields are required", "red"))
    exit()

try:
    age = int(age)
except ValueError:
    print(colored("Error: Age must be a number", "orange"))
    exit()

if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print(colored("Error: Email address is not valid", "red"))
    exit()

if len(password) < 8:
    print(colored("Error: Password must be at least 8 characters long", "red"))
    exit()

# Write the data to a JSON file
data = {
    'name': name,
    'age': age,
    'email': email,
    'password': password
}

with open('jsonuserregistration.json', 'a') as jsonfile:
    json.dump(data, jsonfile)
    jsonfile.write('\n')
    print(colored("Success: Data is Verified", "green"))

# Print the footer
print(colored("=" * 40, "magenta"))
print(colored(" " * 13 + "THANK YOU!" + " " * 13, "white", "on_magenta", attrs=["bold"]))
print(colored("=" * 40, "magenta"))

# Run jsonlogin.py
os.system('python jsonlogin.py')