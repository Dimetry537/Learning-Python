import random

def score(dice):
    score =[]
    while len(score) < 6:
        dice = random.randint(1, 6)
        for dice in score:
            print(dice)
            
score(1)