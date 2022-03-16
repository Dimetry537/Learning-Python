import random

print("I will add up the numbers you give me.") 

value = 0

while True:
    number = int(input('Enter the value: '))
    value = number + value
    print('The total so far is: ' + str(value))
    if number == 0:
        break

print('The total is: ' + str(value))
    