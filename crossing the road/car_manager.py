import random
from turtle import Turtle
COLOR = ["red", "blue", "yellow", "violet", "pink", "orange"]
STARTING_POSITION = 10
MOVE_DISTANCE = 5
turtle = Turtle()


class CarManager:
    def __init__(self):
        self.all_cars = []
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.color(random.choice(COLOR))
            new_car.shapesize(stretch_wid=2, stretch_len=1)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(STARTING_POSITION)
