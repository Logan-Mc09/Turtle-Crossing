from turtle import Turtle, Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import random
import time


screen = Screen()
screen.bgcolor("grey")
screen.setup(width=600,height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player_position = (0, -280)

player = Player(position = (0, -280))
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.car_spawn()
    car.drive()

    # Detect collision with car object
    for i in car.all_cars:
        if i.distance(player) < 20:
            scoreboard.game_end()
            game_is_on = False

    # Detect if player has made it to the end of the map
    if player.is_at_end():
        scoreboard.add_point()
        player.go_to_start()
        car.level_up()

screen.exitonclick()