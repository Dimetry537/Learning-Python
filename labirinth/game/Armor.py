from .Item import Item

class Armor(Item):
    def __init__(self, name, protection) -> None:
        self.name = name
        if protection < 0 and protection > 1:
            raise ValueError('Invalid protection in armor')
        self.protection = protection

    def absorb(self, damage: int) -> int:
        return (1 - self.protection) * damage