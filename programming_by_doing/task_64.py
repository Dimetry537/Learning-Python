print("Type in a message, and I'll display it several times.")

message = input("Message: ")

n = int(input("How many times you want to display message: "))

for i in range(n):
    print(str(i+1) + ") " + message)