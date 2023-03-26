from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Da snake game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.update()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_state = True
while game_state:

    snake.move()
    screen.update()
    sleep(0.1)

    if snake.head.distance(food) < 15:
        snake.eat()
        food.refresh()
        score.scoreboard_add()

    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        score.reset()
        snake.reset()

    for body in snake.snake_list[1:]:
        if snake.head.distance(body) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
