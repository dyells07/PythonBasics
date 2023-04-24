file = open("ep29file.txt", "w",encoding="utf-8")
file.write("Hello World")
value = ("the answer", 42)   #yesma hamile for lagayera user input lekhna sakchau
s= str(value)
file.write(s)
with open('ep29file.txt', 'r') as file:
    content = file.read()

print(content)
file.close()