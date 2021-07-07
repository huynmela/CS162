# Author: Melanie Huynh
# Date: 27 January 2021
# Description: This program sorts a list of strings using the insertion sort method.

def string_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)): # indexing through the list
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos].lower() > value.lower(): #case insensitive, compare words
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


#a = ["a","A", "z", "C", "qwearry"]
#string_sort(a)
#print(a)
