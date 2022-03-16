import random
print('HERE COMES THE DICE!')

roll_1 = float("nan")
roll_2 = float("nan")

while roll_1 != roll_2:
    roll_1 = random.randrange(1, 6)
    roll_2 = random.randrange(1, 6)
    roll_total = roll_1 + roll_2
    print('roll #1: ' + str(roll_1))
    print('roll #2: ' + str(roll_2))
    print('The total is: ' + str(roll_total))
    if roll_1 == roll_2:
        break
        