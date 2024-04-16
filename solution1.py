class Circle:
    '''
    Class of circles
    '''
    all_circles = []
    pi = 3.1415

    def __init__(self, radius=1):
        '''
        method for initialization
        :param radius: radious of circle
        '''
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self):
        '''
        method of counting area of circle
        :return: area of circle
        '''
        return Circle.pi * self.radius ** 2

    @staticmethod
    def total_area():
        '''
        method of counting area of all circles
        :return: area of all circles
        '''
        sq = 0
        for i in range(len(Circle.all_circles)):
            sq += Circle.area(Circle.all_circles[i])
        return sq

    def __str__(self):
        '''
        method for string representation
        :return: radius of circle
        '''
        return str(self.radius)

    def __repr__(self):
        '''
        method for interactive presentation
        :return: radius of circle
        '''
        return self.__str__()
