# the GUI application is inspired by this blog post from Fahadul Shadhin
# https://python.plainenglish.io/build-a-sorting-algorithm-visualizer-in-python-f6f4afb1c98a

from tkinter import *
from tkinter import ttk
import random
from sortalgos.sort_draw import *


WHITE = "#ffffff"
L_GRAY = "#f4f4f4"
GRAY = "#ececec"
D_GRAY = "#c8c8c8"
L_BLUE = "#5cabfa"
ORANGE = "#ff5100"
win_width = 900
win_height = 600
canvas_frame_height = 400
x_pad = 2
y_pad = 2
list_len = 100

unsorted = []

# setup window
w = Tk()
w.geometry(str(win_width) + "x" + str(win_height))
w.maxsize(win_width, win_height)
w.config(bg = WHITE)    #white background
w.title("Visualize Sorting Algorithms")

algo_name = StringVar() #tkinter string variable
algo_label = ["Bubble Sort", "Selection Sort", "Insertion Sort"]

speed_name = StringVar() #tkinter string variable
speed_label = ["Slow", "Fast", "No Delay"]

# populate the array with unsorted random data
def create_random_list():
    global unsorted

    unsorted = []
    for i in range(0, list_len):
        v = random.randint(1,150)
        unsorted.append(v)

    draw(unsorted, [L_BLUE for c in range(len(unsorted))], win_width-x_pad*8, canvas_frame_height-y_pad*2)

# sets the sorting speed
def set_speed():
    if speed_menu.get() == "Slow":
        return 0.5
    elif speed_menu.get() == "Fast":
        return 0.1
    else:
        return 0

# starts the sorting
def start_sorting():
    global unsorted
    tick = set_speed()

    if algo_menu.get() == "Bubble Sort":
        bubble_sort(unsorted, draw, tick)
    elif algo_menu.get() == "Selection Sort":
        selection_sort(unsorted, draw, tick)
    elif algo_menu.get() == "Insertion Sort":
        selection_sort(unsorted, draw, tick)

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

# canvas frame
top_frame = Frame(w, width = (win_width-x_pad*2), height = canvas_frame_height, bg = GRAY, bd = 3)
top_frame.grid(row = 0, column = 0, padx = x_pad, pady = y_pad)
# UI frame
bottom_frame = Frame(w, width = (win_width-x_pad*2), height = (win_height-canvas_frame_height-y_pad*4), bg = GRAY, bd = 3)
bottom_frame.grid(row = 1, column = 0, padx = x_pad, pady = y_pad, sticky = "nsew")

# algorithm selection menu
label1 = Label(bottom_frame, text = "Sorting Algorithm: ", bg = GRAY)
label1.grid(row = 0, column = 0, padx = 10, pady = 5, sticky="w")
algo_menu = ttk.Combobox(bottom_frame, textvariable = algo_name, values = algo_label)
algo_menu.grid(row = 0, column = 1, padx = 5, pady = 5)
algo_menu.current(0)

# speed selection menu
label2 = Label(bottom_frame, text = "Draw Speed: ", bg = GRAY)
label2.grid(row = 1, column = 0, padx = 10, pady = 5, sticky="w")
speed_menu = ttk.Combobox(bottom_frame, textvariable = speed_name, values = speed_label)
speed_menu.grid(row = 1, column = 1, padx = 5, pady = 5)
speed_menu.current(0)

# generate random array button
gen_button = Button(bottom_frame, text = "Generate Random Array", command=create_random_list, bg = D_GRAY)
gen_button.grid(row = 0, column = 3, padx = 10, pady = 5, sticky = "e")
# start sorting and drawing
sort_button = Button(bottom_frame, text = "Sort and Draw", command=start_sorting, bg = D_GRAY)
sort_button.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = "e")

# canvas
canvas = Canvas(top_frame, width = (win_width-x_pad*8), height = (canvas_frame_height-y_pad*2), bg = L_GRAY)
canvas.grid(row = 0, column = 0, padx = x_pad, pady = y_pad)
# draw window
w.mainloop()
