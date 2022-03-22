number = int(input("write a number: "))

for i in range(number):
    i += 1
    print(i , end= ",")
    
list = [i]
    
print("The sum is: " + str(sum(list)))