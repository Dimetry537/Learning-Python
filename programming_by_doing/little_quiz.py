origin = input("Are you ready for a quiz? (input: yes or no)")

if origin == "no":
    exit("You are loose")
if origin == "yes":
    print("Okay, here it comes!")
else:
    exit("Your answer is not correct")

print('''
Q1) What is the capital of Alaska?
	1) Melbourne
	2) Anchorage
	3) Juneau
''')


