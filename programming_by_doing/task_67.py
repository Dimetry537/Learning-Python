#pylint:disable=W0104
x = int(input("counting from: "))
y = int(input("counting to: "))
z = int(input("counting by: "))

for i in range(x, y + 1, z):
    
    print (i)