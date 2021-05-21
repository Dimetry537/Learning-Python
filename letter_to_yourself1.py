print('напишите своё имя')
name = input()
print('напишите свой адрес')
adress = input()
lenght_name = int(len(name))
lenght_adress = int(len(adress))
x = '-'
lenght_score = lenght_name if lenght_name > lenght_adress else lenght_adress
print(lenght_score)