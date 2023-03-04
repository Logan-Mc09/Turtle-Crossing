from turtle import Turtle
import random

COLORS = ["green yellow","red","black","white","blue","yellow","pink","purple"]

MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE 
    # Creates car objects; to keep too many car objects from spawning restricts the creation of new objects to if random.randint == 1
    def car_spawn(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    # Moves car object to other side of the screen
    def drive(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    # increases speed of car objects after clearing a level
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
