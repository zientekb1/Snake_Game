from turtle import Turtle
TURTLE_LOCATION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class _Snake:

    def __init__(self):
        self.segments = []  # hold the turtles that make up the snake
        self.create_snake()  # create 3 squares to make the snake
        self.head = self.segments[0]  # front of the snake

    def create_snake(self):
        for turtle_index in TURTLE_LOCATION:
            self.add_segment(turtle_index)

    # create the turtle to add to the snake
    def add_segment(self, turtle_index):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(turtle_index)
        self.segments.append(tim)

    # takes the snake and moves it completely off the screen and creates another one
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # add the newly created turtle to the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # the snake is constantly moving
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # if the user presses the up key the snake moves up and cannot move down
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # if the user presses the down key the snake moves down and cannot move up
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # if the user presses the left key the snake moves to the left and cannot move right
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # if the user presses the right key the snake moves right and cannot move left
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
