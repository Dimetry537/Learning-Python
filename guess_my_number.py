# написать программу, которая будет угадывать число

print("Guess a number from 0 to 1000, the estimated value will be indicated")

beginning = 0

end = 1000

middle_value = (beginning + end) // 2

guessed_value = None

while True:
    print("I guess it's: ")
    print(middle_value)
    guessed_value = input("Enter '>' if the value is bigger or '<' smaller than guessed value, if the value is right enter '=': ")
    if guessed_value == "=":
        print("I guess your value")
        break
    elif guessed_value == "<":
        beginning = middle_value
    elif guessed_value == ">":
        end = middle_value
    else:
        print("Let's try to enter '<', '>' or '=' to continue")
        continue
    middle_value = (beginning + end) // 2
    