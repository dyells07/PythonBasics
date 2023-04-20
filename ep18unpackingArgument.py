b=list(range(3,6))
print(b)

args=[3,6]
print(list(range(*args)))

#lambda Expression
def a(n):
    return lambda x:x*n

f=a(2)
print(f(3))


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
