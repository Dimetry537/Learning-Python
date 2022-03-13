from calendar import weekday


print('''Weekday 1: Sunday
Weekday 2: Monday
Weekday 3: Tuesday
Weekday 4: Wednesday
Weekday 5: Thursday
Weekday 6: Friday
Weekday 7: Saturday
Weekday 0: Saturday
''')
weekday = int(input("Enter weekday number: "))

if weekday == 1:
    print('Today is Sunday!')
elif weekday == 2:
    print('Today is Monday!')
elif weekday == 3:
    print('Today is Tuesday!')
elif weekday == 4:
    print('Today is Wednesday!')
elif weekday == 5:
    print('Today is Thursday!')
elif weekday == 6:
    print('Today is Friday!')
elif weekday == 7 or weekday == 0:
    print('Today is Saturday!')
else:
    print('Error')