basket={'apple', 'banana', 'orange', 'grape', 'pineapple'}
print(basket)
print('orange' in basket)
print('mango' in basket)

a=set('abracadabra')
print(a)
b=set('alacazam')
print(b)
print(a-b)

b={x for x in 'abracadabra' if x not in 'abc'}
print(b)