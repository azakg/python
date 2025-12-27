class Rectangle:
    def __init__(self, width = 1, hight = 2):
        self.__width = width
        self.__hight = hight

    def getArea(self):
        area = self.__width * self.__hight
        return area

    def getPerimeter(self):
        p = (self.__width + self.__hight)*2
        return p