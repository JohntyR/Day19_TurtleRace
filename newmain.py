from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.title("Turtle Race!")
screen.setup(width=500, height=400)

turtle_colours = ["red", "blue", "green", "yellow", "purple", "orange"]

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Pick a colour:\n red, blue, green, yellow, purple, orange",
)
print(user_bet)

if user_bet == None:
    screen.bye()


turtle_racers = []

for i in range(6):
    turtle_racers.append(Turtle(shape="turtle"))


for i, t in enumerate(turtle_racers):
    t.penup()
    t.color(turtle_colours[i])
    y_pos = -90 + (i * 30)
    t.goto(x=-235, y=y_pos)

if user_bet:
    is_race_on = True


while is_race_on:
    for i, t in enumerate(turtle_racers):
        rand_distance = randint(0, 13)
        t.forward(rand_distance)
        if t.pos()[0] > 230:
            is_race_on = False
            winner = i
            break

if user_bet.lower() == turtle_colours[winner].lower():
    result = screen.textinput(title="You won!", prompt="Bye!")
else:
    result = screen.textinput(title="You lose!", prompt="Bye!")

screen.bye()

screen.exitonclick()