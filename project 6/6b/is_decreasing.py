# Author: Melanie Huynh
# Date: 10 February 2021
# Description: This program is a recursive function that takes a list of numbers and returns True if the
# elements of the list are strictly decreasing, False if otherwise.

def is_decreasing(a_list):
    """
    Returns True when a list of number is strictly decreasing, False if otherwise.
    """
    return helper_is_decreasing(a_list, 0)

def helper_is_decreasing(a_list, pos):
    """
    Helper function recusively passing both the list and the number zero for the position
    """
    # Base case
    if pos == len(a_list) - 1:
        return True
    # Recursive function
    elif a_list[pos] > a_list[pos + 1]: # checks to see if the first position is greater than the second
        return helper_is_decreasing(a_list, pos + 1)
    else: # if the above if fails, the list is not strictly decreasing
        return False
# TESTING
#a_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#a_list = [1, 9]
#a_list = [10, 9, 8, 7, 10, 2]
#print(is_decreasing(a_list))

