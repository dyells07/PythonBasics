def scope_test():
    def do_local():
        spam = "local spam"
        print("It is Accesible here:", spam)
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        
    def do_global():
        global spam
        spam = "global spam"
        
        
    spam = "test spam"
    do_local()
    print("After local assignment:", spam) # Output: After local assignment: test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam) # Output: After nonlocal assignment: nonlocal spam
    do_global()
    print("After global assignment:", spam) # Output: After global assignment: nonlocal spam
    
scope_test()
print("In global scope:", spam) # Output: In global scope: global spam



# it is just a simple example of how to use the class and the object in python by using nested function