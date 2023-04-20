tel = {'jack':400,'sape':300}
tel['guido'] = 500
print(tel)
print(tel['jack'])


a=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(a)


#looping through a dictionary
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v)