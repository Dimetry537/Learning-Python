up_wall = '---'
lateral_wall = '|'
spaces = '   '
horizont_wall = [up_wall*10]
for i in range(len(horizont_wall)):
    print(horizont_wall[i])
vertical_wall = [lateral_wall + spaces*9 + lateral_wall]
for k in range(len(vertical_wall)):
    print(vertical_wall[k])