
class Draw:
    def __init__(self, obj):
        self.obj = obj
    def drawFigure(self, angle):
        for i in range(0, angle):
            angleOwn = 360 / angle
            self.obj.forward(100)
            self.obj.right(angleOwn)

