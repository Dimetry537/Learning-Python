from .Item import Item

class Weapon(Item):
    def __init__(self, name, damage) -> None:
        self.name = name
        if damage < 1 and damage > 20:
            raise ValueError('Invalid damage of weapon')
        self.damage = damage
            
    def hit(self) -> int:
        return self.damage