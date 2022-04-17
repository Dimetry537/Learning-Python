import random

def score(dice):
    dice = []
    for dice in range(5):
        roll = random.randint(1, 6)
        for roll in dice:
            dice.append(roll)
            print(dice)

score(dice=5)