class Stack:
    def __init__(self) -> None:
        self.items = []

    def pop(self):
        if len(self.items) == 0:    
            return
        return self.items.pop()   

    def top(self):
        if len(self.items) == 0:    
            return
        return self.items[len(self.items -1)]

    def push(self, item):
        self.items.append(item)