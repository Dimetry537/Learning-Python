#import random
#def score(dice):
#    dice = []

#    for i in range(5):
#        i = random.randint(1, 6)
#        dice.append(i)
#    print(dice)
#    return dice

score_not_random = [1, 1, 1, 5, 5, 5]

counter = 0
triplet = 0

for numbers in score_not_random:
    
    triplet += 1
    
    if numbers == 1 and triplet == 3:
        counter += 1000
        print(counter)
        
for k in score_not_random:
        
    triplet += 1
        
    if k == 5 and triplet == 3:
        counter += 500
        print(counter)
    
#    elif numbers == 5 and triplet < 3:
#        counter += 50
#        print(counter)
#    
#    elif numbers == 1 and triplet < 3:
#        counter += 100
#        print(counter)
#    
#    elif numbers == 6 and triplet == 3:
#        counter += numbers * 100
#        print(counter)
        
    
#def score(dice): 
#    score = 0 

#    tallies = {}.fromkeys(set(dice),0) # {1:0, 5:0}
#    for die in dice:
#        tallies[die] += 1#{1:3, 5:2}
#    
#    if 1 in tallies and tallies [1] >= 3:
#        tallies[1] -= 3
#        score += 1000
#    
#    for k in tallies:
#        if tallies[k] >= 3:
#            tallies[k] -= 3
#            score += k * 100

#    for k in tallies:
#        if k == 1:
#            score += 100 * tallies[k]
#        elif k == 5:
#            score += 50 * tallies[k]
#        
#    return score
#    
#print(score([]))