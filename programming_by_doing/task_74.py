number = int(input("write a number: "))

s = 0

for i in range(number):
    i += 1
    s += i
    print(i , end= ",")
    
print("The sum is: " + str(s))