from turtle import Turtle

START_POSITION = [0,-280]
FINISH_LINE = 280
class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    # moves player object forward
    def move(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
    
    def game_over(self):
        self.text.write("GAME OVER", align="center", font=("Courier", 80, "normal"))

    # returns true/false depending on whether the player object reaches the end or is hit by a car
    def is_at_end(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
        
    def go_to_start(self):
        self.goto(START_POSITION)
