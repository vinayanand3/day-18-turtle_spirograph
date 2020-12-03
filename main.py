import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("classic")

# draw random polygon shapes
# def draw_shape(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.fd(100)
#         tim.rt(angle)
#
#
# for shape_sides in range(3, 10):
#     tim.color(random.choice(colors))
#     draw_shape(shape_sides)

# random walk

t.pensize(2)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


tim.speed("fastest")


def draw_spirograph(number_of_circles):
    for _ in range(int(360 / number_of_circles)):
        tim.color(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + number_of_circles)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
