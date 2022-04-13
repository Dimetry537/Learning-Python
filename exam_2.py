# теорема пифагора,
class Triangle:
    
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def pifagor(self):
        return self.__a**2 == self.__b**2 + self.__c**2

    def __repr__(self):
        return str(self.__a) + " " + str(self.__b) + " " + str(self.__c)

    def square(self):
        return (self.__a * self.__b)/2

class Polygon:
    def __init__(self):
        self.triangle_list = []

    def add(self, triangle):
        self.triangle_list.append(triangle)
    
    def big_triangles(self, value):
        for i in self.triangle_list:
            if i.square() > value:
                print(i)

# найти треунольники из списка triangle_list у которых площадь больше value
#начально значение triangle_list[0]
# конечное значение 

# начальное значение 0
# конечное 100
# шаг единиц
# мыслить атомными значениями
# сдедующий этап мыслить объектами
                
def generate_right_triangle():
    for a in range(1, 101, 1):
        for b in range(1, 101, 1):
            for c in range(1, 101, 1):
                t = Triangle(a, b, c)
                if t.pifagor():
                    yield(t)

polygon = Polygon()
for t in generate_right_triangle():
    polygon.add(t)
    
polygon.big_triangles(4799)
