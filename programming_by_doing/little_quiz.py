origin = input("Are you ready for a quiz? (input: yes or no)")

if origin == "no":
    exit("You are loose")
if origin == "yes":
    print("Okay, here it comes!")
else:
    exit("Your answer is not correct")

q1 = int(input('''
Q1) What is the capital of Alaska?
	1) Melbourne
	2) Anchorage
	3) Juneau
'''))

if q1 == 2:
    print("That's right!")
else:
    print("This answer is not  correct")

q2 = int(input('''
Q2) Can you store the value "cat" in a variable of type int?
	1) yes
	2) no
'''))

if q2 == 1:
    print('''Sorry, "cat" is a string. ints can only store numbers.''')
else:
    print("That's right!")

q3 = int(input('''
Q3) What is the result of 9+6/3?
	1) 5
	2) 11
	3) 15/3
'''))

if q3 == 2:
    print("That's correct!")
else:
    print("This answer is not  correct")

# if q1 == 2 and q2 == 2 and q3 == 2:
#     print("Overall, you got 3 out of 3 correct.")
# if q1 == 1 and q2 == 2 and q3 == 2:
#     print("Overall, you got 2 out of 3 correct.")

exit('Thanks for playing!')