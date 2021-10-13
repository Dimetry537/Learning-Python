name = input("Hey, what's your name? ")
x = "Ok, " + name + " how old are you? "
age = int(input(x))

if age <= int(16):
    k = "You can't drive, " + name
    print(k)

if age <= int(18):
    l = "You can't vote, " + name
    print(l)

if age <= int(25):
    m = "You can't rent a car, " + name
    print(m)

if age >= int(26):
    n = "You can do anything that's legal, " + name
    print(n)