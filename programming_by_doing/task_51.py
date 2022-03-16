print("Type in a message, and I'll display it several times.")
message = input("Message: ")
counter = int(input("how many times to display the message?: "))
counter_control = 0

while True:
    counter_control += 1
    print(str(counter_control)+ "0)" + message)
    if counter_control == counter:
        break