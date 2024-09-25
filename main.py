import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(fun=player.move_player, key='w')


def collision_verification():
    for n in car_manager.car_list:
        if player.distance(n) < 20:
            scoreboard.game_over_screen()
            return True
    return False


def score_verification():

    if player.ycor() > 280:
        player.points += 1
        scoreboard.score_update(player.points)
        player.goto(0, -280)
        car_manager.increase_speed()



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    score_verification()
    car_manager.create_car()
    car_manager.move_car()

    if collision_verification():
        game_is_on = False

screen.exitonclick()