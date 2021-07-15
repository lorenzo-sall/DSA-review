# recursively draw a fractal tree
import turtle
import random

# takes a starting lenght for the branch, an angle for each smaller branch and a turtle
# as arguments
# recursively draw each branch (every branch is similar)
def draw_tree(branch_len, angle, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(angle)
        draw_tree(branch_len - 15, angle, t)
        t.left(angle * 2)
        draw_tree(branch_len - 15, angle, t)
        t.right(angle)
        t.backward(branch_len)

# takes a starting lenght for the branch, an angle for each smaller branch and a turtle
# as arguments
# recursively draw each branch. each branch has different lenght and the angles are
# randomized. the color of the branch depends on its lenght
def draw_rand_tree(branch_len, angle, t):

    random.seed()
    branch_len = branch_len * random.randint(80, 120) / 100
    angle = angle * random.randint(80, 120) / 100
    if branch_len > 50:
        t.color("brown")
    else:
        t.color("green")

    if branch_len > 5:
        t.forward(branch_len)
        t.right(angle)
        draw_rand_tree(branch_len - 15, angle, t)
        t.left(angle * 2)
        draw_rand_tree(branch_len - 15, angle, t)
        t.right(angle)
        t.up()
        t.backward(branch_len)
        t.down()

my_t = turtle.Turtle()
win = turtle.Screen()

my_t.left(90)
my_t.up()
my_t.backward(300)
my_t.down()

draw_rand_tree(80, 20, my_t)
win.exitonclick()
