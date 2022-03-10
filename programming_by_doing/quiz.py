print('''
TWO QUESTIONS!
Think of an object, and I'll try to guess it.
''')

print('Question 1) Is it animal, vegetable, or mineral?')

answer = input('answer is: ')

print('Question 2) Is it bigger than a breadbox?')

answer_breadbox = input('answer is: ')

if answer == 'animal' and answer_breadbox == 'yes':
	answer_end = 'mouse'

if answer == 'animal' and answer_breadbox == 'no':
	answer_end = 'squirrel'

if answer == 'vegetable' and answer_breadbox == 'yes':
	answer_end = 'watermelon'

if answer == 'vegetable' and answer_breadbox == 'no':
	answer_end = 'carrot'

if answer == 'mineral' and answer_breadbox == 'yes':
	answer_end = 'paper clip'
	
if answer == 'mineral' and answer_breadbox == 'no':
	answer_end = 'Camaro'
	
print('''
My guess is that you are thinking of a ''' + answer_end + '''.
I would ask you if I'm right, but I don't actually care.
''')