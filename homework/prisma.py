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
            exit("your parameter is wrong")
            