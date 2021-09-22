from .item import Item
from typing import Union

class Inventory:
    def __init__(self) -> None:
        self.items = []
        self.size = 20

    def add(self, item: Item) -> bool:
        if self.size > len(self.items):
            self.items.append(item)
            return True
        else:
            return False

    def find(self, name) -> Union[Item, None]:
        try:
            return self.items[self.items.index(name)]
        except ValueError:
            return None

    def remove(self, name) -> bool:
        try:
            self.items.remove(name)
            return True
        except ValueError:
            return False

    def free_space(self) -> int:
        return self.size - len(self.items)


    def __repr__(self) -> str:
        if len(self.items) == 0:
            return "Inventory is empty with free space of " + str(self.free_space())
        output = ""
        for item in self.items:
            output += item.name + ", "
        return "Inventory of " + output + "with free space of " + str(self.free_space())