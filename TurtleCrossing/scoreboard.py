from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        #self.game_over = "GAME OVER"
        self.update_scoreboard()
        
        
    # updates score as player progresses through the levels
    def update_scoreboard(self):
        self.clear()
        self.goto(0,230)
        self.write(f"Level: {self.score}", align="center", font=("Courier", 20, "normal"))

    # adds one point to overall score once player object reaches the end
    def add_point(self):
        self.score+=1
        self.update_scoreboard()
    # End game screen; displays highscore
    def game_end(self):
        self.clear()
        self.write(f"GAME OVER\nHIGHSCORE: {self.score}", align="center", font=("Courier", 20, "normal"))