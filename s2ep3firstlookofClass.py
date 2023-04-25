#class ClassName:
#    <statement-1>
#    .
#    .
#    .
#    <statement-N>    #this is a simpe layout of a class

#let me clear the concept of self in python class 


# class MyClass:
#     def __init__(self, x):
#         self.x = x
        
#     def my_method(self):
#         print("The value of x is:", self.x)
        
# a = input("Enter the value of x: ")      
# obj = MyClass(int(a))
# obj.my_method()


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def bark(self):
#          print("\033[33m{} barks!\033[0m".format(self.name))
        
# name = input("\n\033[32mEnter the name of the dog:\033[0m ")
# if not name.isalpha():
#     print("\033[31mError: Name should only contain alphabetic characters.\033[0m")
#     exit()
# age = input("\n\033[32mEnter the age of the dog:\033[0m ")   
# my_dog = Dog(name,int(age))
# my_dog.bark() 

import random
import csv
import json
from termcolor import cprint

class Cat:
    kinds = ["Siamese", "Persian", "Sphynx", "Maine Coon", "Bengal", "Russian Blue"]
    mammals = ["feline", "canine", "bovine", "equine", "ovine"]
    diets = ["carnivorous", "omnivorous", "herbivorous"]

    def __init__(self, name, age):
        self.name = name
        self.age = age
        #random used for random choices
        self.kind = random.choice(self.kinds)
        self.mammal = random.choice(self.mammals)
        self.diet = random.choice(self.diets)

#to taking user input
name = input("\033[35mEnter the name of the cat: \033[0m")
while not name.isalpha():
    print("\033[31mError: Name must only contain alphabetic characters.\033[0m")
    name = input("\033[35mPlease enter a valid alphabetic name: \033[0m")
age = int(input("\033[35mEnter the age of the cat: \033[0m"))
#creating Object
cat = Cat(name, age)

#this is styled format of showing
cprint(" " * 20 + "CAT INFO" + " " * 20, "white", "on_magenta", attrs=["bold", "underline"])
print("")
print(f"\033[36m{'Name:':<12}\033[0m\033[1m{cat.name}\033[0m")
print(f"\033[36m{'Age:':<12}\033[0m\033[1m{cat.age}\033[0m")
print(f"\033[36m{'Kind:':<12}\033[0m\033[1m{cat.kind}\033[0m")

print(f"\033[36m{'Mammal:':<12}\033[0m\033[1m{cat.mammal}\033[0m")

#this is for color coding the diet of cat
if cat.diet == "carnivorous":
    print(f"\033[36m{'Diet:':<12}\033[0m\033[1m\033[41m{cat.diet}\033[0m")
elif cat.diet == "herbivorous":
    print(f"\033[36m{'Diet:':<12}\033[0m\033[1m\033[42m{cat.diet}\033[0m")
else:
    print(f"\033[36m{'Diet:':<12}\033[0m\033[1m\033[43m{cat.diet}\033[0m")
cprint(" " * 53, "white", "on_magenta")

# to store the data in csv file
with open("cat.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([cat.name, cat.age, cat.kind, cat.mammal, cat.diet])

# to store the data in json file
cat_dict = {"name": cat.name, "age": cat.age, "kind": cat.kind, "mammal": cat.mammal, "diet": cat.diet}
try:
    with open("cat.json", "a") as jsonfile:
        json.dump(cat_dict, jsonfile)
        jsonfile.write("\n")
except IOError as e:
    print(f"Error: Unable to write to file 'cat.json': {e}")
#print(cat_dict)