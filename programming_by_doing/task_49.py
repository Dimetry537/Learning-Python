import random

guess = int(input('Guess the number from 0 to 10; you have 7 attempts: '))

number = random.randint(0, 100)

counter = 0

while True:
    if guess < number:
        counter +=1
        guess = int(input('Your number is less than expected (' + str(counter) + '): '))
    elif guess > number:
        counter += 1
        guess = int(input('Your number is higher (' + str(counter) + ') : '))
    else:
        exit('you guessed')

if counter == 7:
    exit("you've run out of attempts")
