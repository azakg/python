import  math
class Circle:
    def __init__(self, radius = 1, color = 'black'):
        self.radius = radius
        self.color = color
    def getPerimeter(self):
        return 2 * self.radius * math.pi
    def getArea(self):
        return self.radius * self.radius * math.pi

    # def setRadius(self, radius):
    #     self.radius  = radius

