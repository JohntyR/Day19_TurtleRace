from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_clockwise():
    tim.right(10)


def turn_anticlockwise():
    tim.left(10)


def reset():
    tim.reset()
    tim.clear()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_anticlockwise)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkeypress(key="c", fun=reset)


screen.exitonclick()