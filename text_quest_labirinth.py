labirinth = {0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3]}
x = labirinth
rules = 'Hello, Adventure, welcome to Minotaurs labirinth. You must find exit from this labirinth and dont get caught by the minotaur. You must write in the console: left, right, up, down to go through the labirinth. Also You can write exit if you want go out from the programm, but must remember, that if back here You will start over. if you agree with the rules, write yes, if write no you will exit'
print(rules)
yes = input()
if yes == 'yes':
	pass
if yes == 'no':
	exit()
route = 'where will You go'
print(route)
x = labirinth[0][0]
input(x)
if x 