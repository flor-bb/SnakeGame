from turtle import Turtle

# will create the first 3 squares of the snake as a constans
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_tale(pos)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_tale(self, pos):
        new_segment = Turtle("square")
        new_segment.speed("fastest")
        new_segment.color("blue")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        self.add_tale(self.segments[-1].position())

    def up(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(-180)

    def right(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(0)
