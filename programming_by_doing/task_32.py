print('''
TWO QUESTIONS!
Think of an object, and I'll try to guess it.
''')

print('Question 1) Is it animal, vegetable, or mineral?')

answer = input('answer is: ')

print('Question 2) Is it bigger than a breadbox?')

answer_breadbox = input('answer is: ')

if answer == 'animal':
	if answer_breadbox == 'yes':
		answer_end = 'mouse'
	else:
		answer_end = 'squirrel'

if answer == 'vegetable':
	if answer_breadbox == 'yes':
		answer_end = 'watermelon'
	else:
		answer_end = 'carrot'

if answer == 'mineral':
	if answer_breadbox == 'yes':
		answer_end = 'paper clip'
	else:
		answer_end = 'Camaro'
	
print('''
My guess is that you are thinking of a ''' + answer_end + '''.
I would ask you if I'm right, but I don't actually care.
''')