square = [1,2,3,8,9,10,15,16,17]

print('for printing list we have to use print(square) and for printing first 3 elements of list we have to use print(square[0:3])')
print(square)
print(square[0:3])
print(square[-1])

print("\nwe can add for elements in list like this square.append(4) and we can add multiple elements in list like this square.extend([5,6,7])")
square.append(4)
print(square)
square.extend([5,6,7])
print(square)

print("\nwe can remove elements from list like this square.pop() and we can remove specific element from list like this square.pop(2)")
square.pop()
print(square)
square.pop(2)
print(square)
