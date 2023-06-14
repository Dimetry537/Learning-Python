import random

class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vertex({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def generate_maze(width, height):
    maze = {}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def visit(vertex):
        x, y = vertex.x, vertex.y
        if vertex not in maze:
            maze[vertex] = [0, 0, 0, 0]

        for i, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy
            neighbor = Vertex(new_x, new_y)
            if 0 <= new_x < width and 0 <= new_y < height and neighbor not in maze:
                maze[vertex][i] = 1
                visit(neighbor)

    visit(Vertex(0, 0))
    return maze

width = 5
height = 5
maze = generate_maze(width, height)
for vertex, directions in maze.items():
    print(f"{vertex}: {directions}")
