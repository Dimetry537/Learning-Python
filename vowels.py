vowels = ['a', 'e', 'i', 'o', 'u']
word = input('enter word: ')
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in found:
    print(vowels)
help(list)