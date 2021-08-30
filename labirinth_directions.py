from vertex import Vertex
# labirinth = {Vertex(0, 0): [1,5],
# Vertex(0,1):[0,2],
# Vertex(0,2):[1,3],
# Vertex(0,3):[4,2],
# Vertex(1,3):[3,37],
# Vertex(1,0):[0,6,7],
# Vertex(1,1):[5],
# Vertex(2,0):[5,8],
# Vertex(2,1):[7,9],
# Vertex(3,1):[8,10],
# Vertex(3,2):[9,11,12],
# Vertex(3,3):[10,37],
# Vertex(4,2):[10,13],
# Vertex(5,2):[12,14,16,17],
# Vertex(5,1):[13,15],
# Vertex(6,1):[14],
# Vertex(6,2):[13],
# Vertex(5,3):[13,18],
# Vertex(6,3):[17,19],
# Vertex(7,3):[18,20],
# Vertex(7,4):[19,21],
# Vertex(7,5):[20,22],
# Vertex(6,5):[21,23],
# Vertex(6,6):[22,24],
# Vertex(6,7):[23,25],
# Vertex(5,7):[24,26],
# Vertex(4,7):[25,27],
# Vertex(3,7):[26,28,36],
# Vertex(3,8):[27,29],
# Vertex(4,8):[28,30],
# Vertex(4,9):[29,31],
# Vertex(4,10):[30,32],
# Vertex(5,10):[31],
# Vertex(2,4):[34,37],
# Vertex(2,5):[33,35],
# Vertex(3,5):[34,36],
# Vertex(3,6):[27,35],
# Vertex(2,3):[4,11,33]}
# directions = [
# ['up', 'right'],
# ['left', 'right'],
# ['left', 'right'],
# ['right', 'up'],
# ['up', 'down'],
# ['up', 'right', 'down'],
# ['left'],
# ['down', 'right'],
# ['up', 'left'],
# ['down', 'right'],
# ['up', 'left', 'right'],
# ['down', 'left'],
# ['up', 'down'],
# ['down', 'left', 'right'],
# ['up', 'right'],
# ['down'],
# ['down'],
# ['up', 'left'],
# ['up', 'down'],
# ['down', 'right'],
# ['right', 'left'],
# ['down', 'left'],
# ['up', 'right'],
# ['right', 'left'],
# ['down', 'left'],
# ['up', 'down'],
# ['up', 'down'],
# ['up', 'left', 'right'],
# ['up', 'left'],
# ['down', 'right'],
# ['right', 'left'],
# ['up', 'left'],
# ['down'],
# ['right', 'left'],
# ['up', 'left'],
# ['down', 'right'],
# ['right', 'left'],
# ['up', 'down', 'right']]

##
##
##   (1,0) -- (1,1)
##     |
##   (0,0) -- (0,1)
##

# vartex: [up, left, right, down], -1 no actiono
labirinth = {
    Vertex(0,0): [2, -1, 1, -1],
    Vertex(0,1): [-1, 0, -1, -1],
    Vertex(1,0): [-1, -1, 3, 0],
    Vertex(1,1): [-1, 2, -1, -1],
} # exit 0, 2, 3
# directions = [
#     ['right', 'up'],
#     ['left'],
#     ['down', 'right'],
#     ['left'],
# ]

mapping = ['up', 'left', 'right', 'down'];

start_index = 0
start_vertex = list(labirinth)[start_index]

finish_index = 3

index = start_index
current_vertex = start_vertex
while True:
    path = (input('Please select direction (up, down, right, left)'))

    if path in mapping:
        index_path = mapping.index(path)
        index = labirinth[current_vertex][index_path]
        if index == -1:
            print("You can't go there, stupid!")
            continue
        current_vertex = list(labirinth)[index]
        if current_vertex == list(labirinth)[finish_index]:
            exit('You win')
        print('You moved to room ', index)
    else:
        print("You can't go there, stupid!")