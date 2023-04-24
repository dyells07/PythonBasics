import csv
import os
import getpass

# Read the data from the CSV file
with open('formvalidation.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    #print(data)

# Prompt the user to enter their email and password
email = input("Enter your email address: ")
password = getpass.getpass("Enter your password: ")

# Check if the email and password match
for row in data:
    if row[2] == email and row[3] == password:
        print("\033[32mLogin successful!\n\n\033[0m")
        break
else:
    print("\033[31mInvalid email or password.\033[0m")
    while True:
        choice = input("Do you want to try again? (y/n): ")
        if choice.lower() == 'y':
            email = input("Enter your email address: ")
            password = getpass.getpass("Enter your password: ")
            for row in data:
                if row[2] == email and row[3] == password:
                    print("\033[32mLogin successful!\n\n\033[0m")
                    break
            else:
                print("\033[31mInvalid email or password.\033[0m")
        elif choice.lower() == 'n':
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
<<<<<<< HEAD

os.system('python rock.py')
=======
                 
os.system('python rock.py')
>>>>>>> 1a4a4102cb2ef4997527dad96a97824357b14e3f
