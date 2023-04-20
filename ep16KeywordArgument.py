def greet(name="", message="Hello"):
    user_name = input("What's your name? ")
    user_message = input("What message would you like to send? ")
    if user_name:
        name = user_name
    if user_message:
        message = user_message
    print(message + ", " + name)

greet() # use default message "Hello"
greet(name="user", message="bye!") # use custom message "Hey"
