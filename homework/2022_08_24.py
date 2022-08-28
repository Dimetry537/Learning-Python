#pylint:disable=E0101
# цель: Написать один класс полностью самостоятельно
# 1 Задача: написать функцию расчета площади комнаты по высоте, ширине, длине (всех поверхностей)
# 2 Задача: добавить задачу 1 через класс (class Room, 3 поля класса)
# 3* Задача: добавить метод сравнение  комнат между собой по площади (равно не равно - def __eq__ подсказка)

class Room():
    def __init__(self, width: int, length: int, height: int) -> None:
        self.width = width
        self.length = length
        self.height = height
        self._volume = width * length * height
        
    def volume(self):
        return self._volume
        
p = Room(1, 2, 3)

p.volume()

print(p)
print(p.volume)