import random
dice = []
for i in range(5):
        i = random.randint(1, 6)
        dice.append(i)

print(dice)

dict_dise = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}

for ordered_dict in dice:
    dict_dise[ordered_dict] += 1

#dict_dise = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 0}

k = list(dict_dise.values())
    
print("\n")
    
print(dict_dise)

print("\n")

counter_1 = 0
counter = 0
couples = 0
troika = 0

for i in dict_dise.values():
    if i == 1:
        counter_1 += 1
    elif i == 2:
        counter += 1
        if counter == 1:
            couples = 1
        elif counter == 2:
            couples = 2
    elif i == 3:
        troika = 1
    elif i == 4:
        exit("four of a kind")
    elif i == 5:
        exit("Yatze")
        

if couples == 1 and troika == 1:
    exit("Full House")
elif couples == 2:
    print("two pairs")
elif couples == 1:
    print("pair")
elif troika == 1:
    print("troika")
    
if counter_1 == 5 and k[0] == 0 or counter_1 == 5 and k[-1] == 0:
    print("Street")
