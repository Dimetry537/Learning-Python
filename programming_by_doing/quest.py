print('''
WELCOME TO MITCHELL'S TINY ADVENTURE!
''')

print('''
You are in a creepy house!  Would you like to go "upstairs" or into the
"kitchen"?
''')

player = input('Where do you go? ')

if player == 'kitchen':
    player_k = input('''There is a long countertop with dirty dishes everywhere.
    Off to one side there is, as you'd expect, a refrigerator.
    You may open the "refrigerator" or look in a "cabinet".''')
    if player_k == 'refrigerator':
        player_ref = input('''
        Inside the refrigerator you see food and stuff.  It looks pretty nasty.
        Would you like to eat some of the food? ("yes" or "no")
        ''')
        if player_ref == 'yes':
            exit('You ate, got poisoned and died! Game over:-)')
        elif player_ref == 'no':
            exit('You died of hunger:-)')
    elif player == 'cabinet':
        player_cab = input('You find strange letter. You want to open it ("yes" or "no")?')
        if player_cab == 'yes':
            exit('You find map about exit from this house and you won this game, congratulations!!!')
        elif player_cab == 'no':
            exit('you were eaten by a monster behind your back')

elif player == 'upstairs':
    player_u = input('''Upstairs you see a hallway.
    At the end of the hallway is the master "bedroom".
    There is also a "bathroom" off the hallway.
    Where would you like to go?''')
    if player_u == 'bathroom':
        exit('You went into the water, in which there was an electric cable, you were electrocuted.')
    elif player_u == 'bedroom':
        exit('The door closed tightly and you died a few days later.')