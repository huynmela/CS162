# Author: Melanie Huynh
# Date: 10 Feb 2021
# Description: This is a recursive function that takes a list of numbers and returns
# the maximum value in the list

def list_max(a_list):
    """
    Returns the maximum number of a list using recursion by slicing the list
    """
    # base case states that if the list contains only one number, that is the max
    if len(a_list) == 1:
        return a_list[0]
    else:
    # slice the list and return the max by looking at everything after an index
        if list_max(a_list[1:]) > a_list[0]: #if at the position the number is greater than the one before it
            return list_max(a_list[1:]) # return the number
        else:
            return a_list[0] # else return the number at the position

# TESTING
#a_list = [1, 200, 9, 10, 100, 3, 2, 100, 1]
#print(list_max(a_list))
