# define the snake class
from turtle import Turtle

SNAKE_BODY_PART = 3
MOVE_DISTANCE = 20
STARTING_POSITION = [(-20, 0), (-40, 0), (-60, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.head = Turtle()

        self.create_snake()

        # create segments

    def create_snake(self):

        self.head.speed(0)
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.head.goto(0, 0)
        self.segments.append(self.head)
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
        # if len(self.segments) > 0:
        #     self.segments[0].goto(self.head.xcor(), self.head.ycor())

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):

        # Hide the segments
        for segment in self.segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        self.segments.clear()
        self.head = Turtle()
        # Create segments
        self.create_snake()
