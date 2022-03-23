number = int(input("write a number: "))

s = 0

for i in range(1, number + 1):
    s += i
    if i == number:
        print(i)
    else:
        print(i , end= ",")
    
print("The sum is: " + str(s))