for i in range(1, 10):
    print(i)
 
 
print("\nin range we can also use step like this")   
for i in range(1, 10, 2):
    print(i)
    
    
a=[1,2,3,4,5,6,7,8,9]
for i in range(len(a)):
    print(i,a[i])
    
print("\nwe can also use else in for loop like this")   
print("It simply finds the prime numbers between 1 to 100")
for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            
            break
    else:
        # loop fell through without finding a factor
        print("\n")
        print(n, 'is a prime number')