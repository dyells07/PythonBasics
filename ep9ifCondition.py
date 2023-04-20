a = int(input("Enter your age:"))

if a < 0:
    a = 0
    print('Negative number is not allowed')
elif a < 18:
    print('You are not eligible for voting')
elif a >= 18:
    print('You are eligible for voting')

print('Done') 