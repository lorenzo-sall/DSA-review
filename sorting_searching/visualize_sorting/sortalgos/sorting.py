# implementing different sorting algorithms

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

# short bubble sort checks if any aexchange has been made in a pass and
# if not it terminates because the list is sorted
def short_bubble_sort(l):
    exchange = True
    pass_n = len(l) - 1
    while pass_n > 0 and exchange:
        exchange = False
        for i in range(pass_n):
            if l[i] > l[i + 1]:
                exchange = True
                l[i], l[i + 1] = l[i + 1], l[i]
        pass_n = pass_n - 1

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

# shell sort (diminishing increments sort)
# breaks the list into smaller sublists, each sorted used insertion sort
# shell sort creates sublists taking all items separated by a specific gap
# sorting the sublists reduces the number of of comparisons necessary to sort the whole list
def shell_sort(l):
    subl_count = len(l) // 2
    while subl_count > 0:
        for start_pos in range(subl_count):
            gap_insertion_sort(l, start_pos, subl_count)
        #print("After increments of size", subl_count, "The list is", l)
        subl_count = subl_count // 2

#this implementation of insertion sort is used in shell_short() with incremental gaps
def gap_insertion_sort(l, start_pos, gap):
    for i in range(start_pos + gap, len(l), gap):
        current_v = l[i]
        pos = i

        while pos >= gap and l[pos - gap] > current_v:
            l[pos] = l[pos - gap]
            pos = pos - gap
        l[pos] = current_v

# merge sort
# the list is split in halves recursively until len = 0 and then the elements are confronted and merged back together
# with the right implementation it is O(n log(n)) but with memory usage = n
def merge_sort(l):
    #print("[log]: splitting ", l)
    if len(l) > 1:
        mid = len(l) // 2
        # the slice operator is O(len(slice))
        # passing the indices to the merge function would improve performance to O(n log(n))
        left_l = l[:mid]
        right_l = l[mid:]

        merge_sort(left_l)
        merge_sort(right_l)

        left_c = 0
        right_c = 0
        list_c = 0

        # put back items from the halves to the main list
        while left_c < len(left_l) and right_c < len(right_l):
            if left_l[left_c] < right_l[right_c]:
                l[list_c] = left_l[left_c]
                left_c = left_c + 1
            else:
                l[list_c] = right_l[right_c]
                right_c = right_c + 1
            list_c = list_c + 1
        #print("[log]: while1 ", left_c, right_c, list_c)

        # collect left leftover if any
        while left_c < len(left_l):
            l[list_c] = left_l[left_c]
            left_c = left_c + 1
            list_c = list_c + 1
        #print("[log]: while2 ", left_c, right_c, list_c)

        # collect right leftover if any
        while right_c < len(right_l):
            l[list_c] = right_l[right_c]
            right_c = right_c + 1
            list_c = list_c + 1
        #print("[log]: while3 ", left_c, right_c, list_c)

    #print("[log]: merging ", l)

# quick sort
# uses divide and conquer approach and less additional memory is used but there is loss of performance if
# the list is not divided in half
# a pivot value is chosen (the split point). this point is used to partition the
# list for subsequent calls of quick sort
# when the split point is found items are moved to the appropriated side of the list
# average performance O(n log(n))
# worst case performance O(n^2) if the pivot is too skewed
def quick_sort(l):
    quick_sort_helper(l, 0, len(l) - 1)

# recursively sorts the list, if len(list) = 1 it is already sorted
def quick_sort_helper(l, first_i, last_i):
    if first_i < last_i:
        split_point = partition(l, first_i, last_i)

        quick_sort_helper(l, first_i, split_point - 1)
        quick_sort_helper(l, split_point + 1, last_i)

# implements the pivot choice and the partitioning: two moving marks are used
# left mark is moved to the right until value>pivot
# right mark is moved left until value<pivot
# swap the items and continue moving the marks and repeat until the marks cross, move the pivot to its place and
# return the right mark to split the list in two
def partition(l, first_i, last_i):
    pivot_val = l[first_i] #this implementation takes the first item as pivot. another common method is the median of three
    lm = first_i + 1    #left mark
    rm = last_i         #right mark

    completed = False

    while not completed:
        # move the left mark
        while lm <= rm and l[lm] <= pivot_val:
            lm = lm + 1
        # move right mark
        while rm >= lm and l[rm] >= pivot_val:
            rm = rm - 1

        if rm < lm:
            completed = True    #marks crossed
        else:
            l[lm], l[rm] = l[rm], l[lm] #swap values at marks if out of place

    l[first_i], l[rm] = l[rm], l[first_i]   #swap pivot and right mark values

    return rm

if __name__ == "__main__":

    test = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(test)
    print(test)

    test = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    short_bubble_sort(test)
    print(test)

    test = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(test)
    print(test)

    test = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(test)
    print(test)

    test = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    gap_insertion_sort(test, 0, 1) # equivalent to simple insertion sort
    print(test)

    test = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(test)
    print(test)

    test = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(test)
    print(test)

    test = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(test)
    print(test)
