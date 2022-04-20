import random

def score(dice):

    dice = []

    for i in range(5):
        i = random.randint(1, 6)
        dice.append(i)
    print(dice)
    
score([])


