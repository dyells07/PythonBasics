class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("The animal makes a sound")

class Dog(Animal):# Dog inherits from Animal
    def bark(self):
        print("The dog barks")

my_dog = Dog("Fido")
print(my_dog.name) # Output: Fido
my_dog.bark() # Output: The dog barks
my_dog.make_sound() # Output: The animal makes a sound

class one:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("I am one")

class two:
    def feed_youn(self):
        print("I am two")

class into(one, two):
    def bark(self):
        print("I am into")

my_dog = into("Fido")
print(my_dog.name) # Output: Fido
my_dog.bark() # Output: The dog barks
my_dog.make_sound() # Output: The animal makes a sound
my_dog.feed_youn() # Output: The mammal feeds its young

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("The dog barks")

class Cat(Animal):
    def meow(self):
        print("The cat meows")

my_dog = Dog("Fido")
print(my_dog.name) # Output: Fido
my_dog.bark() # Output: The dog barks
my_dog.make_sound() # Output: The animal makes a sound

my_cat = Cat("Mittens")
print(my_cat.name) # Output: Mittens
my_cat.meow() # Output: The cat meows
my_cat.make_sound() # Output: The animal makes a sound

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("The animal makes a sound")

class Mammal(Animal):
    def feed_youn(self):
        print("The mammal feeds its young")

class Dog(Mammal):
    def bark(self):
        print("The dog barks")

my_dog = Dog("Fido")
print(my_dog.name) # Output: Fido
my_dog.bark() # Output: The dog barks
my_dog.make_sound() # Output: The animal makes a sound
my_dog.feed_youn() # Output: The mammal feeds its young

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("The animal makes a sound")

class Mammal:
    def feed_youn(self):
        print("The mammal feeds its young")

class Dog(Animal, Mammal):
    def bark(self):
        print("The dog barks")

my_dog = Dog("Fido")
print(my_dog.name) # Output: Fido
my_dog.bark() # Output: The dog barks
my_dog.make_sound() # Output: The animal makes a sound
my_dog.feed_youn() # Output: The mammal feeds its young

