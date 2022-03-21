message = input("What is your message? ")

print("Your message is " + str(len(message)) + " characters long.")

list = [message]

a = list.index(0)

print(a)

print("The first character is at position 0 and is 'A'.")

print("The last character is at position 30 and is '!'.")

print("Here are all the characters, one at a time: ")

counter = 0

for i in message:
    counter += 1
    print(str(counter) + ") - " + i)