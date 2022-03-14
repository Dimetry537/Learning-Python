print('''
WELCOME TO THE BANK OF MITCHELL.
''')

correct_pin = 1234

while True:
    enter_pin = int(input('Enter your pin: '))
    if enter_pin == correct_pin:
        exit('Your pin is correct, access is allowed')
    else:
        print('Pin isnt correct? try again')
    continue