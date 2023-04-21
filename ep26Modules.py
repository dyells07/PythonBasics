import ep7fibonacci as f
import sys
import builtins


result = f.ep7fibonacci(100)
print(result)

print(sys.version)#for checking the version of python
#for importing a module we can also use this method you have to make a file named which is imported and write the code in that file and then import it in the file where you want to use it


#let's talk about dir() function which is used to find the list of all the functions and variables in a module
#for example:
print(dir(f)) 
print(dir(builtins))#this will give you the list of all the functions and variables in the builtins module