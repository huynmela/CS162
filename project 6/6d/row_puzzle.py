# Author: Melanie Huynh
# Date: 10 February 2021
# Description: This program is a puzzle consisting of a row of squares with nonnegative
# integers with a zero in the rightmost square. The objective is to move a token from
# left or right exactly onto the last zeroth square. Amount of moves is dependent
# on what integer the token lands on within a square.

def row_puzzle(a_list):
    """
    Return True if the token lands on the zero square on the right most spot, False
    if otherwise.
    """
    return helper_row_puzzle(a_list, 0, memo=None)

def helper_row_puzzle(a_list, pos, memo=None):
    """
    Helper function for row_puzzle function which runs the recursive process with positions
    """
    # Must check to see if a spot has been visited
    if memo is None:
        memo = {}
    if pos not in memo:

        # Base case, exit condition based on if you are at the end of the list
        if pos == len(a_list) - 1:
            return True
        if a_list[pos] == 0: # If the square is a zero, it is a deadzone
            return False
        # Recursion
        # Define l and r variables to be mutated in the if statements
        l = False
        r = False
        # Look to the left
        if pos - a_list[pos] > 0:
            memo[pos] = a_list[pos]
            l = helper_row_puzzle(a_list, pos - a_list[pos], memo)
        # Look to the right
        if pos + a_list[pos] < len(a_list):
            memo[pos] = a_list[pos]
            r = helper_row_puzzle(a_list, pos + a_list[pos], memo)
        # Then check to see if the either recursive move is true
        if l == True or r == True:
            return True
        # Otherwise, the list is false
        return False

# TESTING
#print("this one should work")
#print(row_puzzle([2, 4, 5, 3, 1, 3, 1, 4, 0]))
#print(row_puzzle([1, 1, 1, 0]))
#print(row_puzzle([1, 2, 4, 6, 3, 1, 3, 3, 1, 1, 0]))

#print("this shouldn't work")
#print(row_puzzle([1, 3, 2, 1, 3, 4, 0]))
#print(row_puzzle([1, 1, 0, 1, 0]))
#print(row_puzzle([0, 2, 4, 5, 0]))
