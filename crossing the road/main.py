from turtle import Screen
from car_manager import CarManager
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("white")
screen.listen()

car = CarManager()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    car.create_car()


screen.exitonclick()