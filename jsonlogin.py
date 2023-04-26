import json
import os
import getpass
from termcolor import colored

# Print the header
print(colored("=" * 40, "magenta"))
print(colored(" " * 15 + "LOGIN" + " " * 15, "white", "on_magenta", attrs=["bold"]))
print(colored("=" * 40, "magenta"))

# Read the data from the JSON file
with open('jsonuserregistration.json') as jsonfile:
    data = [json.loads(line) for line in jsonfile]

# Prompt the user to enter their email and password
email = input(colored("Enter your email address: ", "yellow"))
password = getpass.getpass(colored("Enter your password: ", "yellow"))

# Check if the email and password match
for row in data:
    if row['email'] == email and row['password'] == password:
        print(colored("Login successful!\n", "green"))
        break
else:
    print(colored("Invalid email or password.", "red"))
    while True:
        choice = input(colored("Do you want to try again? (y/n): ", "cyan"))
        if choice.lower() == 'y':
            email = input(colored("Enter your email address: ", "yellow"))
            password = getpass.getpass(colored("Enter your password: ", "yellow"))
            for row in data:
                if row['email'] == email and row['password'] == password:
                    print(colored("Login successful!\n", "green"))
                    break
            else:
                print(colored("Invalid email or password.", "red"))
        elif choice.lower() == 'n':
            break
        else:
            print(colored("Invalid choice. Please enter 'y' or 'n'.", "red"))

# Print the footer
print(colored("=" * 40, "magenta"))
print(colored(" " * 13 + "THANK YOU!" + " " * 13, "white", "on_magenta", attrs=["bold"]))
print(colored("=" * 40, "magenta"))

# Run rock.py
os.system('python snake.py')