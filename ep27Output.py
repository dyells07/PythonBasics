#first of all print() is a function and end is a keyword argument
print("Hello World")


#secondly we can also write the above code like this
#as formatted string literals or f-strings for short
#for example:
a=10
name="Bipin"
print(f'{name} has {a} apples')
#please check the output of the above code in powershell or cmds

import math

print(f'The value of pi is approximately {math.pi:.3f}.')
#where .3f is a format specifier which means that we want to display the value of pi upto 3 decimal places


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
    
#where 10 is a field width which means that we want to display the name in a field of 10 characters and phone in a field of 10 characters

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
#where animals is a variable and this will not display with ascii art but will display the value of the variable
#!a applies ascii(), !s applies str(), and !r applies repr():
#for example:

s = 'Hello, World! 7'
print(f'{s!a}')#this will display the value of s with ascii art
print(f'{s!s}')#this will display the value of s with str()
print(f'{s!r}')#this will display the value of s with repr()

#if we used = instead of : in the format specifier, it forces the field to be used as a keyword argument rather than a positional argument. This lets us type the following:
name="Bipin"
print(f'My name is {name=}.')

#the string format() method
print('We are the {} who say "{}!"'.format('rappers', 'yo'))

#if we do {1} and {0} then the output will be different 
print('{0} and {1}'.format('dyells', 'Bipin'))
print('{1} and {0}'.format('dyells', 'Bipin'))

#let give the index a name
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    #Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
#this is the same as the above code but the above code is more readable

#there is another method called zfill() which pads a numeric string on the left with zeros. It understands about plus and minus signs:
print('12'.zfill(5))
print('-3.14'.zfill(7))