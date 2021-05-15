print('Введите свое имя')
name = input()
print('Введите свой адрес')
adress = input()
x = '-'
y = ' '
vertic_line = '|'
plus = '+'
x_multiplayer = 45
y_multiplayer = 10
tag_multi = 7
start_multi = 10
plus_string = plus + x + plus
string_tag = vertic_line + y*start_multi + '####' + y*tag_multi + vertic_line
space_line = vertic_line + y*x_multiplayer
size_name = int(len(name))
print(plus_string)
print(string_tag)
print(string_tag)
print(string_tag)
print(vertic_line + y*start_multi + name + name_length + vertic_line)
print(vertic_line + y*start_multi + adress + adress_length + vertic_line)
print(space_line + vertic_line)
print(space_line + vertic_line)
print(plus_string)