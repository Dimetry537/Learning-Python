import random

guess = int(input('Guess the number from 0 to 10; you have 5 attempts: '))

number = random.randint(0, 10)

counter = 0

while True:
	counter += 1
	guess = int(input('Try again (' + str(counter) + ') : '))
	if guess < number:
		counter +=1
		guess = int(input('Your number is less than expected (' + str(counter) + '): '))
	elif guess > number:
		counter += 1
		guess = int(input('Your number is higher (' + str(counter) + ') : '))
	else:
		exit('you guessed')
	if counter == 5:
		exit("you've run out of attempts")