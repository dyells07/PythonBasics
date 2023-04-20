def fib(n):
    print("This is a program for Fibonacci series!")
    a, b = 0, 1
    while a < n:
        print(a, end=', ')
        a, b = b, a + b
    print() # print new line

number = int(input("Enter the number of terms: "))
fib(number)
