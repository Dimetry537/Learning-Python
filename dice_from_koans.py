import random

dice = []

for i in range(5):
    i = random.randint(1, 6)
    dice.append(i)

print(dice)

#def score(dice):
#    dice = []
#    for dice in range(5):
#        roll = random.randint(1, 6)
#        for roll in dice:
#            dice.append(roll)
#            print(dice)

#score(5)