# #Fibonacci series:
# print("This is a program for fibonacci series !\n")
# a,b = 0,1
# while b < 10:
#     print(b)
#     a,b = b,a+b
    
# #output:
# print("the output can also written differently like this !\n")
# c=1
# while c < 100:
#     print(c,end=',')
#     a = c
#     c = a+c

def ep7fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=',')
        a, b = b, a+b