from turtle import Turtle
FONT = ("Courier", 16, "normal")
FONTGAMEOVER = ("Courier", 16, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-260,250)
        self.write(f"LEVEL {self.level}", align="left", font=FONT)
        self.level += 1
        print(self.level)

    def game_over(self):
        self.goto(0,0)
        self.write("G A M E   O V E R", align="center", font=FONTGAMEOVER)



