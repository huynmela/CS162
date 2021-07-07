# Author: Melanie Huynh
# Date: 27 January 2021
# Description: This program uses a binary search to find a target. If the target
# is not found, it raises an exception.

def bin_except(a_list, target):
    """
    Searches a_list for an occurrence of target
    If found, returns the index of its position in the list
    If not found, returns -1, indicating the target value isn't in the list
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound

class TargetNotFound(Exception):
    """
    Error raised when a target is not found
    """
    pass

def main():
    """
    Main function for testing bin_except
    """
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 11

    return print(bin_except(a_list, target))

if __name__ == '__main__':
    main()
