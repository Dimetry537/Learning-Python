#pylint:disable=E0101
# цель: Написать один класс полностью самостоятельно
# 1 Задача: написать функцию расчета площади комнаты по высоте, ширине, длине (всех поверхностей)
# 2 Задача: добавить задачу 1 через класс (class Room, 3 поля класса)
# 3* Задача: добавить метод сравнение  комнат между собой по площади (равно не равно - def __eq__ подсказка)

class Room():
    def __init__(self, width: int, length: int, height: int, width_1: int, length_1: int, height_1: int) -> None:
        self.width = width
        self.width_1 = width_1
        self.length = length
        self.length_1 = length_1
        self.height = height
        self.height_1 = height_1
        self.volume = width * length * height
        self.volume_1 = width_1 * length_1 * height_1

    def __eq__(self, o):
        if self.volume > self.volume_1:
            return True
        return False
        
    def __str__(self):
        return str(self.volume) + "    " + str(self.volume_1) + "   " + str(Room.__eq__)
        
p = Room(2, 2, 3, 1, 2, 3)

print(p.volume, p.volume_1, p.__str__)