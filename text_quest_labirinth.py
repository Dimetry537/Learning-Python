labirinth = [[1,2],[2,3],[2,4],[2,5],[3,6],[6,7],[7,2],[7,8],[8,9],[9,5],[9,10]]
x = labirinth[0][0]
rules = 'Hello, Adventure, welcome to Minotaurs labirinth. You must find exit from this labirinth and dont get caught by the minotaur. You must write in the console: left, right, up, down to go through the labirinth. Also You can write exit if you want go out from the programm, but must remember, that if back here You will start over. if you agree with the rules, write yes, but if you are scared, then run the bitch screaming nooo)))'
print(rules)
yes = input()
if yes == 'yes':
	pass
if yes == 'no':
	exit('someone went to wash their pants')
route = 'where will You go'
print(route)
x = input()
if x == 'right':
	print('deadend')
