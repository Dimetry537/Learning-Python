message = input("What is your message? ")

print("Your message is " + str(len(message)) + " characters long.")

first_letter = message[0]

last_letter = message[-1]

print("The first character is at position 0 and is " + str(first_letter))

print("The last character is at position " + str(len(message)) + " and is " + str(last_letter))

print("Here are all the characters, one at a time: ")

counter = 0

for i in message:
    counter += 1
    print(str(counter) + ") - " + i)