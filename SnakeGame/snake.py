from turtle import Turtle
POSITION = ((0, 0), (-20, 0), (-40, 0))
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_list = []
        for pos in POSITION:
            self.add_segment(pos)
        self.head = self.snake_list[0]

    def move(self):
        for segments in range(len(self.snake_list) - 1, 0, -1):
            position = self.snake_list[segments - 1].pos()
            self.snake_list[segments].goto(x=position[0], y=position[1])
        self.snake_list[0].forward(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def add_segment(self, pos):
        s = Turtle(shape='square')
        s.penup()
        s.color('white')
        s.setposition(pos)
        self.snake_list.append(s)

    def eat(self):
        final_segment = self.snake_list[-1].pos()
        self.add_segment(final_segment)

    def reset(self):
        for segments in range(len(self.snake_list)):
            self.snake_list[segments].goto(x=1000, y=1000)
        self.snake_list.clear()
        for pos in POSITION:
            self.add_segment(pos)
        self.head = self.snake_list[0]

