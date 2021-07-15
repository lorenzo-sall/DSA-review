# check if a word is a palindrome using the deque abstract data type implemented in adts.py

import adts

def check_palindrome(in_string):
    char_deque = adts.Deque()

    for c in in_string:
        char_deque.add_rear(c)

    is_palindrome = True

    while char_deque.size() > 1 and is_palindrome == True:
        if char_deque.remove_rear() != char_deque.remove_front():
            is_palindrome = False

    return is_palindrome


print(check_palindrome("abcde"))
print(check_palindrome("abba"))
print(check_palindrome("radar"))
print(check_palindrome("notforsure"))
