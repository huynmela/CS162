# Author: Melanie Huynh
# Date: 10 February 2021
# Description: This program recursively takes two string parameters and returns
# True if thefirst string is a subsequence of the second string, False otherwise.

def is_subsequence(str_1, str_2):
    """
    Returns True if the first string is a subsequence of the second string, False otherwise.
    """
    return helper_is_subsequence(str_1, str_2, 0, 0)

def helper_is_subsequence(str_1, str_2, pos_1, pos_2):
    """
    Helper function for is_subsequence function which runs the recursive process with positions
    """
    # Base case
    if pos_1 == len(str_1):
        return True
    if pos_2 == len(str_2):
        return False
    # Recursion
    if str_1[pos_1] == str_2[pos_2]: # checks to see if the letters match
        pos_1 += 1 # if they do, move to next letter
    return helper_is_subsequence(str_1, str_2, pos_1, pos_2 + 1) # then check again

#Testing
#str_1 = "eh"
#str_2 = "hell"

#print(is_subsequence(str_1, str_2))
