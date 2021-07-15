# searching an item in an ordered list. return True if found, else False
# we find the item in the middle and compare. if it is not our item, we know that
# smaller items will be in the first half of the list and bigger items will be in the
# second half. we split the list and repeat until wi find the item or the list is exhausted
# (divide and conquer)
# the binary search is O(log(n)) in the worst case

def binary_search(in_list, e):
    first_i = 0
    last_i = len(in_list) - 1
    found = False

    while first_i < last_i and not found:
        mid_i = (first_i + last_i) // 2
        if in_list[mid_i] == e:
            found = True
        else:
            if e < in_list[mid_i]:
                last_i = mid_i - 1
            else:
                first_i = mid_i + 1

    return found


test_list = list(range(20))

print(test_list)
print(binary_search(test_list, 12))
print(binary_search(test_list,42))
