from math import pi
square=[]
for x in range(10):
    square.append(x**2)
    
print(square)

squares = list(map(lambda x: x**2, range(20)))
print(squares)

# [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print([str(round(pi, i)) for i in range(1, 6)])
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print([[row[i] for row in matrix] for i in range(4)])