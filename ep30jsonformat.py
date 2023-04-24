import json 
x= {'name':'John', 'age':30, 'city':'New York'}
y=json.dump(x, open('ep30jsonformat.json', 'w'))

data =json.loads(x)
print(data['name'])
print(data['age'])
print(data['city'])