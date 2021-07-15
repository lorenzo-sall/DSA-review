# searching an item in an unordered list sequentialy, return True if found, else False
# in the best case scenario the item we want will be the 1st, in the worst case
# it will be the last or not in the list.
# the complexity of this search is O(n)

def sequential_search(in_list, e):
    position = 0
    found = False

    while position < len(in_list) and not found:
        if in_list[position] == e:
            found = True
        else:
            position = position + 1

    return found, position

test_list = list(range(20))

print(test_list)
print(sequential_search(test_list, 12))
print(sequential_search(test_list,42))
