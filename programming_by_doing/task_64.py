print("Type in a message, and I'll display it several times.")

message = input("Message: ")

n = int(input("How many times you want to display message: "))

counter = 0

for i in range(n):
    counter += 1
    print(str(counter) + ") " + message)