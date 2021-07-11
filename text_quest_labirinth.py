labirinth = {[0,0]:[1,5],[0,1]:[0,2],[0,2]:[1,3],[0,3]:[4,2],[1,3]:[3,37],[1,0]:[0,6,7],[1,1]:[5],[2,0]:[5,8],[2,1]:[7,9],[3,1]:[8,10],[3,2]:[9,11,12],[3,3]:[10,37],[4,2]:[10,13],[5,2]:[12,14,16,17],[5,1]:[13,15],[6,1]:[14],[6,2]:[13],[5,3]:[13,18],[6,3]:[17,19],[7,3]:[18,20],[7,4]:[19,21],[7,5]:[20,22],[6,5]:[21,23],[6,6]:[22,24],[6,7]:[23,25],[5,7]:[24,26],[4,7]:[25,27],[3,7]:[26,28,36],[3,8]:[27,29],[4,8]:[28,30],[4,9]:[29,31],[4,10]:[30,32],[5,10]:[31],[2,4]:[34,37],[2,5]:[33,35],[3,5]:[34,36],[3,6]:[27,35],[2,3]:[4,11,33]}
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
print(x)