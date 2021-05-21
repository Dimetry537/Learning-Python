print('Введите свое имя')
name = input()
print('Введите свой адрес')
adress = input()
x = '-'
y = ' '
vertic_line = '|'
plus = '+'
tag = '####'
origin_space = 10
past_space = 2
lenght_name = int(len(name))
lenght_adress = int(len(adress))
lenght_score = max(lenght_name, lenght_adress)
plus_line = plus + x*origin_space + x*lenght_score + x*past_space + plus
tag_line = vertic_line + y*origin_space + y*(lenght_score-4) + tag + y*past_space + vertic_line
name_line = vertic_line + y*origin_space + name + y*(lenght_score - lenght_name) + y*past_space + vertic_line
adress_line = vertic_line + y*origin_space + adress + y*(lenght_score - lenght_adress) + y*past_space + vertic_line
space_line = vertic_line + y*origin_space + y*lenght_score + y*past_space + vertic_line
print(plus_line)
for i in range(3):
    print(tag_line)
print(space_line)
print(name_line)
print(space_line)
print(adress_line)
for n in range(2):
    print(space_line)
print(plus_line)