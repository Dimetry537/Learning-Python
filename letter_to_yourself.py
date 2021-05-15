name = 'Dmitry Maksakov'
adress = 'Somther in our world'
x = '-'
y = ' '
vertic_line = '|'
plus = '+'
x_multiplayer = 30
y_multiplayer = 20
tag_multi = 7
start_multi = 10
plus_string = plus + x*x_multiplayer + plus
string_tag = vertic_line + y*y_multiplayer + '####' + y*tag_multi + vertic_line
space_line = vertic_line + y*y_multiplayer
print(plus_string)
print(string_tag)
print(string_tag)
print(string_tag)
print(vertic_line + y*start_multi + name + vertic_line)
print(vertic_line + y*start_multi + adress + vertic_line)
print(space_line + y*tag_multi + vertic_line)
print(space_line + y*tag_multi + vertic_line)
print(plus_string)
print(len(name))
print(len(adress))