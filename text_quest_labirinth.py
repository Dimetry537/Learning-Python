from vertex import Vertex
labirinth = {Vertex(0, 0):[1,5],
Vertex(0,1):[0,2],
Vertex(0,2):[1,3],
Vertex(0,3):[4,2],
Vertex(1,3):[3,37],
Vertex(1,0):[0,6,7],
Vertex(1,1):[5],
Vertex(2,0):[5,8],
Vertex(2,1):[7,9],
Vertex(3,1):[8,10],
Vertex(3,2):[9,11,12],
Vertex(3,3):[10,37],
Vertex(4,2):[10,13],
Vertex(5,2):[12,14,16,17],
Vertex(5,1):[13,15],
Vertex(6,1):[14],
Vertex(6,2):[13],
Vertex(5,3):[13,18],
Vertex(6,3):[17,19],
Vertex(7,3):[18,20],
Vertex(7,4):[19,21],
Vertex(7,5):[20,22],
Vertex(6,5):[21,23],
Vertex(6,6):[22,24],
Vertex(6,7):[23,25],
Vertex(5,7):[24,26],
Vertex(4,7):[25,27],
Vertex(3,7):[26,28,36],
Vertex(3,8):[27,29],
Vertex(4,8):[28,30],
Vertex(4,9):[29,31],
Vertex(4,10):[30,32],
Vertex(5,10):[31],
Vertex(2,4):[34,37],
Vertex(2,5):[33,35],
Vertex(3,5):[34,36],
Vertex(3,6):[27,35],
Vertex(2,3):[4,11,33]}
rules = '''Hello, Adventure, welcome to Minotaurs labirinth. 
You must find exit from this labirinth and dont get caught by the minotaur. 
You must write in the console: left, right, up, down to go through the labirinth. 
Also You can write exit if you want go out from the programm, 
but must remember, that if back here You will start over. 
if you agree with the rules, write yes, if write no you will exit'''
#описание действий человека, пошагово. записать атомарными действиями. перевести шаги в алгоритм. Действия, условия и состояния. я нахожусь в комнате - состояние. могу ли я идти вправо - вопрос, условие. я иду вправо - действие. начальное состояние это нулевая вершина (position=labirinth.keys()[0]).
#состояние я нахожусь в комнате. Вопрос могу ли я пойти направо. могу ли я пойти налево? могу ли я пойти прямо? могу ли я пойти назад? Действие я прохожу в следующую комнату. Состояние я нахожусь в Х комнате.
#ты находишься в комнате. условия: Справа находится стена, слева находится стена, впереди стена, сзади находится стена. Условие: ты можешь идти.
labirinth_directions = [labirinth.keys()[0]:['up', 'right'],
labirinth.keys()[1]:['left', 'right'],
labirinth.keys()[2]:['left', 'right'],
labirinth.keys()[3]:['right', 'up'],
labirinth.keys()[4]:['up', 'down'],
labirinth.keys()[5]:['up', 'right', 'down'],
labirinth.keys()[6]:['left'],
labirinth.keys()[7]:['down', 'right'],
labirinth.keys()[8]:['up', 'left'],
labirinth.keys()[9]:['down', 'right'],
labirinth.keys()[10]:['up', 'left', 'right'],
labirinth.keys()[11]:['down', 'left'],
labirinth.keys()[12]:['up', 'down'],
labirinth.keys()[13]:['down', 'left', 'right'],
labirinth.keys()[14]:['up', 'right'],
labirinth.keys()[15]:['down'],
labirinth.keys()[16]:['down'],
labirinth.keys()[17]:['up', 'left'],
labirinth.keys()[18]:['up', 'down'],
labirinth.keys()[19]:['down', 'right'],
labirinth.keys()[20]:['right', 'left'],
labirinth.keys()[21]:['down', 'left'],
labirinth.keys()[22]:['up', 'right'],
labirinth.keys()[23]:['right', 'left'],
labirinth.keys()[24]:['down', 'left'],
labirinth.keys()[25]:['up', 'down'],
labirinth.keys()[26]:['up', 'down'],
labirinth.keys()[27]:['up', 'left', 'right'],
labirinth.keys()[28]:['up', 'left'],
labirinth.keys()[29]:['down', 'right'],
labirinth.keys()[30]:['right', 'left'],
labirinth.keys()[31]:['up', 'left'],
labirinth.keys()[32]:['down'],
labirinth.keys()[33]:['right', 'left'],
labirinth.keys()[34]:['up', 'left'],
labirinth.keys()[35]:['down', 'right'],
labirinth.keys()[36]:['right', 'left'],
labirinth.keys()[37]:['up', 'down', 'right']]
###Вход Граф лабиринт неориентированный с одинаковыми длинами ребер
#Вывод Вершины и соединения проход по вершинам
#Моя позиция 0
#Контроль позиции
#Если продвижение по вершине в правильном направлении
#то "перед тобой стена"
#Если перемещение в правильном направлении,
#То смена позиции
#повторный контроль позиции
#Если достигли точки 32 завершение лабиринта.
#def labirinth(vertex):
#	position=labirinth.keys()[0]
#	real_position =
print(rules)
yes = input()
if yes == 'yes':
	pass
if yes == 'no':
	exit()
route = 'where will You go'
print(route)