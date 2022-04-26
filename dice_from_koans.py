#import random

#    dice = []

#    for i in range(5):
#        i = random.randint(1, 6)
#        dice.append(i)
#    print(dice)
#    return dice

#others = [2, 3, 4, 6]

#counter = 0
#triplets = 0

#for numbers in score:
#    triplets += 1
#    if numbers == 5:
#        counter += 50
#        print("we found 5")
#        print(counter)
#    elif triplets == 3 and numbers == 5:
#        counter += 500
#        print("set of 5")
#        print(counter)
#    elif triplets == 3 and numbers == 1:
#        counter += 1000
#        print("set of 1")
#        print(counter)
#    elif triplets == 3 and numbers == others:
#        k += 300
#        print("others")
#        print(k)
#    elif numbers == 1:
#        counter += 100
#        print("found 1")
#        print(counter)
#    else:
#        counter += 0
 
def score(dice): 
    score = 0 

    tallies = {}.fromkeys(set(dice),0) 
    for die in dice:
        tallies[die] += 1
    
    if 1 in tallies and tallies [1] >= 3:
        tallies[1] -= 3
        score += 1000
    
    for k in tallies:
        if tallies[k] >= 3:
            tallies[k] -= 3
            score += k * 100

    for k in tallies:
        if k == 1:
            score += 100 * tallies[k]
        elif k == 5:
            score += 50 * tallies[k]
        
    return score