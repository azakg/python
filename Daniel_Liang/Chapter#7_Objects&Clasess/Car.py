class Car:

    def __init__(self, color = 'White', type = 'sedan'):
        self.color = color
        self.type = type

    def getColor(self):
        return self.color

    def setColor(self, newColor):
        self.color = newColor
    def getType(self):
        return self.type