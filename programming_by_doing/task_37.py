gender = input('What is your gender (M or F): ')
first_name = input('First name: ')
last_name = input('Last name: ')
age = int(input('Age: '))

if gender == 'F' and age >= 17:
    marriage = input('Are you married, ' + first_name + '(y or n)? ')
    if marriage == 'y':
        marriage_end = 'Mrs'
    else:
        marriage_end = 'Ms'
        print('Then I shall call you ' + marriage_end + last_name + '.')
if gender == 'F' and age <= 17:
    print('Then I shall call you ' + first_name + ' ' + last_name + '.')
    
if gender == 'M':
	print('Then I shall call you Mr. ' + last_name + '.')