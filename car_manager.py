COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.car_list = []
        self.level_speed = 0

    def create_car(self):
        random_spawn_chance = random.randint(1, 6)
        if random_spawn_chance == 1:
            new_car = Turtle("square")
            new_car.random_y = random.randint(-230, 230)
            new_car.x_pos = 260
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(new_car.x_pos, new_car.random_y)
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE+self.level_speed)

    def reset_position(self):
        self.goto(self.x_pos, self.random_y)

    def increase_speed(self):
        self.level_speed += 3