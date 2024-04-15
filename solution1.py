class Circle:
    all_circles = []
    pi = 3.1415

    def __init__(self, radius=1):
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self):
        return Circle.pi * self.radius ** 2

    @staticmethod
    def total_area():
        sq = 0
        for i in range(len(Circle.all_circles)):
            sq += Circle.area(Circle.all_circles[i])
        return sq

    def __str__(self):
        return str(self.radius)

    def __repr__(self):
        return self.__str__()
