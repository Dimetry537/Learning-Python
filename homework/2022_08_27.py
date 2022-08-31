import math

class Prisma():
    def __init__(self, parallelepiped_score: float, basis_side: float, height: float, ab_angle: float, ba_angle: float) -> None:
        self.parallelepiped_score = parallelepiped_score
        if parallelepiped_score < 3:
            exit("your parameter is wrong")
        self.basis_side = basis_side
        self.height = height
        self.ab_angle = ab_angle
        self.ba_angle = ba_angle
        if ab_angle + ba_angle != 180:
            exit("the angle must be at least 180 degrees")
            
    def volume(self):
        if self.parallelepiped_score == 3:
            g = float(math.sqrt(3))
            volume = float((g/4) * (self.basis_side ** 2) * self.height) 
        else:
            n = float(math.pi/self.parallelepiped_score)
            tan = float(math.tan(n))
            a = self.basis_side ** 2
            square = float((self.parallelepiped_score * a) / (4 * tan))
            volume = float(square * self.height)
        return volume
    
    def __str__(self):
        return str(f"Prima for <{self.parallelepiped_score}>")
             
             
prisma = Prisma(4, 3, 3, 90, 90)

print(f"{prisma}")
print(f"{prisma.volume()}")

prisma = Prisma(3, 1, 1, 90, 90)

print(f"{prisma}")
print(f"{prisma.volume()}")
