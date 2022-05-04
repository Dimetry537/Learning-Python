#import random
#def score(dice):
#    dice = []

#    for i in range(5):
#        i = random.randint(1, 6)
#        dice.append(i)
#    print(dice)
#    return dice

score_not_random = [5, 5, 5,]

counter_1 = 0
counter_2 = 0
counter_3 = 0
triplet_1 = 0
triplet_2 = 0
triplet_3 = 0

for units in score_not_random:
    triplet_1 += 1
    if units == 1 and  triplet_1 < 3:
        counter_1 += 100
    
    elif units == 1 and triplet_1 == 3:
        counter_1 += 1000
    
for fives in score_not_random:
    triplet_2 += 1
    if fives == 5 and triplet_2 < 3:
        counter_2 += 50
         
    elif fives == 5 and triplet_2 == 3:
        counter_2 += 500

for others in score_not_random:
    triplet_3 += 1
    if others == 2 and triplet_3 == 3:
        counter_3 = 2 * 100
        
    if others == 3 and triplet_3 == 3:
        counter_3 = 3 * 100
        
    if others == 4 and triplet_3 == 3:
        counter_3 = 4 * 100
    
    if others == 6 and triplet_3 == 3:
        counter_3 = 6 * 100
        
counter = counter_1 + counter_2 + counter_3
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