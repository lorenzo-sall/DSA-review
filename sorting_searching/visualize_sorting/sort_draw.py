import time

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
c_w = win_width-x_pad*8
c_h = canvas_frame_height-y_pad*2


'''
# bubble sort
# adjacent items are compared and if [i]>[i+1] they are swapped
# best case performance: O(n)
# worst case performance: O(n^2)
def bubble_sort(l):
    for pass_n in range(len(l)-1, 0, -1):
        for i in range(pass_n):
            if l[i] > l[i + 1]:
                #temp = l[i]
                #l[i] = l[i + 1]
                #l[i + 1] = temp
                l[i], l[i + 1] = l[i + 1], l[i]
'''
def bubble_sort(l, draw, tick):
    for pass_n in range(len(l)-1, 0, -1):
        for i in range(pass_n):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                draw(l, [ORANGE if x == i or x == i+1 else L_BLUE for x in range(len(l))], c_w, c_h)
                if tick > 0:
                    time.sleep(tick)
    draw(l, [L_BLUE for x in range(len(l))], c_w, c_h)

'''
# selection sort searches for the largest (smallest) item and moves it to its place,
# it then looks for the 2nd largest (smallest) item and so on
# best, average and worst case performance: O(n^2)
def selection_sort(l):
    for slot in range(len(l) - 1, 0, -1):
        # find the max
        i_max = 0
        for i in range(1, slot + 1):
            if l[i] > l[i_max]:
                i_max = i
        # swap
        l[slot], l[i_max] = l[i_max], l[slot]
'''
def selection_sort(l, draw, tick):
    for slot in range(len(l) - 1, 0, -1):
        # find the max
        i_max = 0
        for i in range(1, slot + 1):
            if l[i] > l[i_max]:
                i_max = i
            draw(l, [ORANGE if x == i or x == i_max else L_BLUE for x in range(len(l))], c_w, c_h)
            if tick > 0:
                time.sleep(tick)
        # swap
        l[slot], l[i_max] = l[i_max], l[slot]

    draw(l, [L_BLUE for x in range(len(l))], c_w, c_h)

'''
# insertion sort
# best case performance: O(n)
# average and worst case performance: O(n^2)
def insertion_sort(l):
    for i in range(1, len(l)):
        current_v = l[i] #store the current value
        pos = i

        # while values to the left are bigger than the current value shift items to make space for the current value
        while pos > 0 and l[pos - 1] > current_v:
            l[pos] = l[pos - 1]
            pos = pos - 1

        l[pos] = current_v
'''
def insertion_sort(l, draw, tick):
    for i in range(1, len(l)):
        current_v = l[i] #store the current value
        pos = i

        # while values to the left are bigger than the current value shift items to make space for the current value
        while pos > 0 and l[pos - 1] > current_v:
            l[pos] = l[pos - 1]
            pos = pos - 1
            draw(l, [ORANGE if x == i or x == pos else L_BLUE for x in range(len(l))], c_w, c_h)

        l[pos] = current_v

    draw(l, [L_BLUE for x in range(len(l))], c_w, c_h)
