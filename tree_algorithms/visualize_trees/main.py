# the current implementation only draws a simmetric binary tree of the selected height, with random int key for each node
# future versions might rewrite the create_draw_tree and create_subtrees to allow for insertion controlled by the user

# the GUI application is inspired by this blog post from Fahadul Shadhin
# https://python.plainenglish.io/build-a-sorting-algorithm-visualizer-in-python-f6f4afb1c98a

from tkinter import *
from tkinter import ttk
import random
from viztreeimports.binarytree import *


WHITE = "#ffffff"
L_GRAY = "#f4f4f4"
GRAY = "#ececec"
D_GRAY = "#c8c8c8"
L_BLUE = "#5cabfa"
ORANGE = "#ff5100"
win_width = 900
win_height = 600
canvas_frame_height = 500 #530
x_pad = 2
y_pad = 2
list_len = 100

# new tree with root key 0
t = BinaryTree(0)

# setup window
w = Tk()
w.geometry(str(win_width) + "x" + str(win_height))
w.maxsize(win_width, win_height)
w.config(bg = WHITE)    #white background
w.title("Visualize Binary Trees")


#algo_name = StringVar() #tkinter string variable
#algo_label = ["Bubble Sort", "Selection Sort", "Insertion Sort"]

height_name = StringVar() #tkinter string variable
height_label = ["0", "1", "2", "3", "4", "5"]

# recursively create subtrees
def create_subtrees(node, current_height):
    node.ins_l(random.randint(1,10))
    node.ins_r(random.randint(1,10))
    h = current_height - 1
    while h > 0:
        create_subtrees(node.lc, h)
        create_subtrees(node.rc, h)

# create a tree and draw it
def create_draw_tree():
    global t
    h = set_height()
    if h > 0:
        create_subtrees(t, h)

    #draw(unsorted, [L_BLUE for c in range(len(unsorted))], win_width-x_pad*8, canvas_frame_height-y_pad*2)

# sets the height of the tree, check boundaries, max h = 5
def set_height():
    h = int(height_menu.get())
    if h >=0 and h <= 5:
        return h
    else:
        return 0

def draw(t, color, c_w, c_h):
    canvas.delete("all")
    r = 10  # circle radius
    tree_h = t.find_height()

'''
# draw elements of value_list as bars, colours are stored in color_list and
# and depend on the status of the elements during the sorting
def draw(value_list, color_list, c_w, c_h):
    canvas.delete("all")
    #c_w = win_width-x_pad*8
    #c_h = canvas_frame_height-y_pad*2
    bar_w = c_w / (len(value_list) + 1)
    offset = 4
    spacing = 2
    norm_value_list = [i / max(value_list) for i in value_list]

    for i, h in enumerate(norm_value_list):
        x0 = i * bar_w + offset + spacing
        y0 = c_h - h*c_h*0.95
        x1 = (i + 1) * bar_w + offset
        y1 = c_h
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_list[i])

    w.update_idletasks()
'''
# canvas frame
top_frame = Frame(w, width = (win_width-x_pad*2), height = canvas_frame_height, bg = GRAY, bd = 3)
top_frame.grid(row = 0, column = 0, padx = x_pad, pady = y_pad)
# UI frame
bottom_frame = Frame(w, width = (win_width-x_pad*2), height = (win_height-canvas_frame_height-y_pad*4), bg = GRAY, bd = 3)
bottom_frame.grid(row = 1, column = 0, padx = x_pad, pady = y_pad, sticky = "nsew")

# height selection menu
label1 = Label(bottom_frame, text = "Tree Height: ", bg = GRAY)
label1.grid(row = 0, column = 0, padx = 10, pady = 5, sticky="w")
height_menu = ttk.Combobox(bottom_frame, textvariable = height_name, values = height_label)
height_menu.grid(row = 0, column = 1, padx = 5, pady = 5)
height_menu.current(0)

# generate tree button
gen_button = Button(bottom_frame, text = "Generate and Draw", command=create_draw_tree(), bg = D_GRAY)
gen_button.grid(row = 0, column = 3, padx = 10, pady = 5, sticky = "e")

# canvas
canvas = Canvas(top_frame, width = (win_width-x_pad*8), height = (canvas_frame_height-y_pad*2), bg = L_GRAY)
canvas.grid(row = 0, column = 0, padx = x_pad, pady = y_pad)
# draw window
w.mainloop()
