class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show (self):
        print(self.x)
        print(self.y)

    def __str__(self):
        return str(self.x) + " " + str(self.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, o):
        if self.x == o.x and self.y == o.y:
            return True
        return False

    def __repr__(self):
        return str(self.x) + " " + str(self.y)