from turtle import Screen
import time
from crossingpet import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with cars
    for car in car_manager.all_cars:
       if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect player reaches other side
    if player.ycor() > 280:
        game_is_on = True
        player.level_up()
        scoreboard.update_scoreboard()
        car_manager.car_level_up()

screen.exitonclick()