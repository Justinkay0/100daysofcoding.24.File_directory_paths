from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Calibri', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as file:
            score = int(file.read())
            self.highScore = score
        self.penup()
        self.goto(x=0, y=280)
        self.color('white')
        self.hideturtle()
        self.write(arg=f"Score = {self.score}", move= False, align='center', font=('Calibri', 12, 'normal'))

    def scoreboard_add(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High score : {self.highScore}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER, your final score is {self.score}", align=ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.highScore:
            with open('data.txt', mode='w') as file:
                score = str(self.score)
                file.write(score)
            self.highScore = self.score
        self.score = 0
        self.update()
