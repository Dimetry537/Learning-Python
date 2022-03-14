print('''
WELCOME TO THE BANK OF MITCHELL.
''')

correct_pin = 1234
loop_through = 0

while True:
    enter_pin = int(input('Enter your pin: '))
    if enter_pin == correct_pin:
        exit('Your pin is correct, access is allowed')
    elif enter_pin != correct_pin:
        print('Pin isnt correct? try again')
        loop_through += 1
    if loop_through == 3:
        print('Its last chance to enter your pin')
    elif loop_through == 4:
        exit('your account blocked')