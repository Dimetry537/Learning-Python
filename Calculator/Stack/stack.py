class Stack:
    def __init__(self) -> None:
        self.items = []

    def pop(self):
        if len(self.items) == 0:    
            return
        return self.items.pop()            

    def push(self, item):
        self.items.append(item)