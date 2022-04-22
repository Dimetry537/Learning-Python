import random

def score(dice):

    dice = []

    for i in range(5):
        i = random.randint(1, 6)
        dice.append(i)
    print(dice)
    return dice

others = [2, 3, 4, 6]

k = 0

for numbers in score([]):
    if numbers == 5:
        k += 50
        print("we found it")
        print(k)
    elif numbers == 1:
        k += 100
        print("found 1")
        print(k)
    else:
        k += 0

n = 0
        
for sets in score([]):
    n += 1
    if n == 3 and sets == 5:
        print("set 5")
        
    if n == 3 and sets == 1:
        print("set 1")
