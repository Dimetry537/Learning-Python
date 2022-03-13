from sqlite3 import complete_statement


weight = int(input("Please enter your current earth weight: "))

gravity_venus = 0.78
gravity_mars = 0.39
gravity_jupiter = 2.65
gravity_saturn = 1.17
gravity_uranus = 1.05
gravity_neptune = 1.23

print('''
I have information for the following planets:
   1. Venus   2. Mars    3. Jupiter
   4. Saturn  5. Uranus  6. Neptune
''')

planet = int(input("Which planet are you visiting? "))

if planet == 1:
    current_weight = weight * gravity_venus
    print("Your weight would be " + str(current_weight) + " kg's on that planet.")
if planet == 2:
    current_weight = weight * gravity_mars
    print("Your weight would be " + str(current_weight) + " kg's on that planet.")
if planet == 3:
    current_weight = weight * gravity_jupiter
    print("Your weight would be " + str(current_weight) + " kg's on that planet.")
if planet == 4:
    current_weight = weight * gravity_saturn
    print("Your weight would be " + str(current_weight) + " kg's on that planet.")
if planet == 5:
    current_weight = weight * gravity_uranus
    print("Your weight would be " + str(current_weight) + " kg's on that planet.")
if planet == 6:
    current_weight = weight * gravity_neptune
    print("Your weight would be " + str(current_weight) + " kg's on that planet.")