name = input("Hey, what's your name? (Sorry, I keep forgetting.): ")
age = int(input("Ok," + name + ", how old are you? "))

if age < 16:
    print("You can't drive," + name)
if age > 15 and age < 18:
    print("You can drive but not vote, " + name)
if age > 17 and age < 25:
    print("You can vote but not rent a car, " + name)
if age > 24:
    print("You can do pretty much anything, " + name)