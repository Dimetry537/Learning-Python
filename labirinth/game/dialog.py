ROOT_NAME = 'e0'

# TODO: Implement class
# asa first thing you can do a binary tree
class Node:
    def __init__(self, value):
        self.children = [] # up too a million
        self.value = value

    def assign_child(self, node):
        self.children.append(node)

# Non-binary
class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self):
        pass

    def print(self):
        pass
    # root
    # children
    # children + children + children

    def children(self, path):
        pass # specific for our case

class Dialog:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.data = {}
        self.__read()

    def __read(self):
        with open(self.filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            for line in lines:
                key, value = line.split(':')
                self.data[key] = value

    def __repr__(self) -> str:
        return self.__str__()

    def root(self):
        return self.data[ROOT_NAME]

    def player_moves(self, line):
        keys = self.data.keys()

    def __str__(self) -> str:
        return_str = ""
        for key, value in self.data.items():
            return_str += key + ":" + value + "\n"
        return return_str