# this script recursively draws self-similar triangles (sierpinski triangle) taking a
# specified degree and changing fill color for each degree
# we start with a degree of choice and decrement it by one for each level drawn
# the base case for the recursive function occurs when the degree counter reaches 0

import turtle

# this function draws a triangle taking a list of points (represented as a list like [x,y])
# a color and a turtle as arguments
def draw_triangle(p_list, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(p_list[0][0], p_list[0][1]) # goes to p1
    t.down()
    t.begin_fill()
    t.goto(p_list[1][0], p_list[1][1]) # goes from p1 to p2
    t.goto(p_list[2][0], p_list[2][1]) # goes from p2 to p3
    t.goto(p_list[0][0], p_list[0][1]) # goes from p3 to p1
    t.end_fill()

# function to find the mid point between two points
def mid_point(p1, p2):
    return ( (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def draw_sierpinski(p_list, degree, t):
    color_map = ["#ff0000", "#ffa500", "#ffff00", "#008000", "#0000ff", "#4b0082", "#ee82ee"]

    draw_triangle(p_list, color_map[degree % len(color_map)], t)
    if degree > 0:
        draw_sierpinski([p_list[0], mid_point(p_list[0], p_list[1]), mid_point(p_list[0], p_list[2])], degree - 1, t)
        draw_sierpinski([p_list[1], mid_point(p_list[0], p_list[1]), mid_point(p_list[1], p_list[2])], degree - 1, t)
        draw_sierpinski([p_list[2], mid_point(p_list[0], p_list[2]), mid_point(p_list[1], p_list[2])], degree - 1, t)

my_t = turtle.Turtle()
win = turtle.Screen()

points = [[-300, -150], [0, 350], [300, -150]]

draw_sierpinski(points, 7, my_t)
my_t.hideturtle()
win.exitonclick()
