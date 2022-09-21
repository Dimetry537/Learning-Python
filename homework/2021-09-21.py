# кот - с именем
class Cat():
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Кот с именем {self.name}"
        
cat = Cat("Барсик")

print(cat)


# собака с именем и породой
class Dog():
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

    def __repr__(self) -> str:
        return f"Собака с именем {self.name} и породой {self.type}"
        
dog = Dog("Поликарп", "дворняга")

print(dog)


# холодильник фирма, тип, размеры, класс энергосбережение
class Sizes():
    def __init__(self, width, height, depth) -> None:
        self.width = width
        self.height = height
        self.depth = depth

    def __repr__(self) -> str:
         return f"размеры(ШхВхГ): {self.width}x{self.height}x{self.depth}"

class Refrigerator():
    def __init__(self, name: str, type: str, weight: int, heigth: int, width: int, depth: int, eco_type: str) -> None:
        self.name = name
        self.type = type
        self.weight = weight
        self.heigth = heigth
        self.width = width
        self.depth = depth
        self.eco_type = eco_type

    def __repr__(self) -> str:
            return f"Холодильник фирма: {self.name}, тип: {self.type}, размеры(ШхВхГ) и вес: {self.heigth}x{self.width}x{self.depth} & {self.weight}, класс энергосбережения: {self.eco_type}"
        
refrigerator = Refrigerator("Ariston", "капельный", 50, 170, 60, 40, "A+")

print(refrigerator)

# два класса матрасс и кровать
# матрасс размер +  название
# кровать матрас + название + размеры
class Sizes():
    def __init__(self, width, height, depth) -> None:
        self.width = width
        self.height = height
        self.depth = depth

    def __repr__(self) -> str:
         return f"размеры(ШхВхГ): {self.width}x{self.height}x{self.depth}"
         


class Mattress():
    def __init__(self, name: str, sizes: Sizes) -> None:
        self.name = name
        self.sizes = sizes

    def __repr__(self) -> str:
            return f"матрас: {self.name}, {self.sizes}"

class Bed():
    def __init__(self, name: str, sizes: Sizes, mattress: Mattress) -> None:
        self.name = name
        self.sizes = sizes
        self.mattress = mattress

    def __repr__(self) -> str:
            return f"Кровать: {self.name}, {self.mattress}, {self.sizes}"

mattress = Mattress("Atlant", Sizes(180, 30, 200))
bed = Bed('Ormatek', Sizes(190, 60, 210), mattress)

print(bed)