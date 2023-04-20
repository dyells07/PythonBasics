def validate_input(input_str):
    for char in input_str:
        if not char.isalpha():
            raise ValueError("Invalid input: input must contain only alphabetic characters")
    # To be implemented later
    pass

# Test the function
input_str1 = input("Enter a string: ")
input_str2 = input("Enter another string: ")
try:
    validate_input(input_str1)
    print(f"{input_str1} is valid input")
except ValueError as e:
    print(str(e))
    
try:
    validate_input(input_str2)
    print(f"{input_str2} is valid input")
except ValueError as e:
    print(str(e))
