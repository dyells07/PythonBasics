import math

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
print()
# create a list of tuples
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    
print()
# create three lists to be zipped together
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['apple', 'banana', 'cherry']

# zip the lists together
zipped_list = zip(list1, list2, list3)

# iterate through the zipped list and print each tuple
for item in zipped_list:
    print(item)
print()
basket={'apple', 'banana', 'orange', 'grape', 'pineapple'}
for i, v in enumerate(sorted(basket)):
    print(i, v)
    
print()

first_data =[56.2,float('NaN'),51.7,55.3,52.5,float('NaN'),47.8]
filtered_data = []
for value in first_data:
    if not math.isnan(value):
        filtered_data.append(value)
        
print(filtered_data)