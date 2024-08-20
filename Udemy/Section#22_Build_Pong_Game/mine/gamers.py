from turtle import Turtle

STARTING_POSITION_RIGHT = [(475, 20), (475, 0), (475, -20)]
STARTING_POSITION_LEFT = [(-475, 20), (-475, 0), (-475, -20)]

class GamerRight:
    def __init__(self):
        self.segments = []
        self.createGamer()


    def createGamer(self):
        for segment in STARTING_POSITION_RIGHT:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(segment)
            self.segments.append(new_segment)

class GamerLeft:
    def __init__(self):
        self.segments = []
        self.createGamer()


    def createGamer(self):
        for segment in STARTING_POSITION_LEFT:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(segment)
            self.segments.append(new_segment)