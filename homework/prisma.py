#pylint:disable=E0202
import math

class Prisma():
    def __init__(self, parallelepiped_score: int, a_facet: int, b_facet: int, ab_angle: int, ba_angle) -> None:
        self.parallelepiped_score = parallelepiped_score
        if parallelepiped_score < 3:
            exit("your parameter is wrong")
        self.a_facet = a_facet
        self.b_facet = b_facet
        self.ab_angle = ab_angle
        self.ba_angle = ba_angle
        if ab_angle + ba_angle != 180:
            exit("the angle must be at least 180 degrees")
            
    def volume(self):
        if self.parallelepiped_score == 3:
            g = math.sqrt(3)
            self.volume = (g/4) * (self.a_facet ** 2) * self.b_facet
        else:
             n = 180/self.parallelepiped_score
             tan = math.atan(n)
             a = self.a_facet ** 2
             square = (self.parallelepiped_score * a) / 4 * tan
             self.volume = square * self.b_facet
    
    def __str__(self):
        return str(self.volume)
             
             
prisma = Prisma(5, 3, 3, 90, 90)
volume = Prisma.volume

print(f"{prisma}")
print(f"{volume}")