# recursively draw a spiral
import turtle

# takes turtle and initial lenght as arguments
def draw_spiral(t, l):
    if l > 0:
        t.forward(l)
        t.right(90)
        draw_spiral(t, l - 5)

my_t = turtle.Turtle()
win = turtle.Screen()

draw_spiral(my_t, 200)
win.exitonclick()
