from colorama import Fore, Back, Style

print("This is a program for calculating age from Birthyear !\n")
birthyear = input("Enter your birthyear:")
print("Datatype of birthyear is " + str(type(birthyear)))
#in there we have to convert string to integer so we have to use int() function for converting string to integer
age = 2023 - int(birthyear)
print("Datatype of age is" + str(type(age)))
#in there we have to convert integer to string so we have to use str() function for converting integer to string

print("\nYour age is " + Fore.RED + str(age)+ Style.RESET_ALL + " years old !\n")



