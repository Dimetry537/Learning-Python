import random
print('HERE COMES THE DICE!')

roll_1 = random.randint(1, 6)
roll_2 = random.randint(1, 6)
roll_total = roll_1 + roll_2

while True:
    if roll_1 == roll_2:
        break
    print('roll #1: ' + str(roll_1))
    print('roll #2: ' + str(roll_2))
    print('The total is: ' + str(roll_total))
        