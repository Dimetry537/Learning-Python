print('''
WELCOME TO MITCHELL'S TINY ADVENTURE!
''')

print('''
You are in a creepy house!  Would you like to go "upstairs" or into the
"kitchen"?
''')

player = input('Where do you go? ')

if player == 'kitchen':
	if player == 'upstairs':
		print('''
Upstairs you see a hallway.  At the end of the hallway is the master "bedroom". There is also a "bathroom" off the hallway.  Where would you like to go?
''')
	else:
		print('''
There is a long countertop with dirty dishes everywhere.  Off to one side there is, as you'd expect, a refrigerator. You may open the "refrigerator" or look in a "cabinet".
''')
