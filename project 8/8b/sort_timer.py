# Author: Melanie Huynh
# Date: 2/24/2021
# Description: This program calculates and compares the amount of time it takes for
# bubble sort and insertion sort to sort through a list, then plots the comparison

import time
import random
import matplotlib.pyplot as pyplot
import functools

def sort_timer(func):
    """
    Decorator function that times how many seconds it takes for func to run
    """
    @functools.wraps(func)
    def wrapper(val):
        """
        Wrapper function that returns elapsed time for sorting
        """
        start_time = time.perf_counter() # begin the timer
        func(val) # then run the function using values
        end_time = time.perf_counter() # end the timer
        elapsed_time = end_time - start_time
        return elapsed_time
    return wrapper

@sort_timer
def bubble_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp

@sort_timer
def insertion_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value

def compare_sorts(bubble, insert):
    """
    Creates a plot comparing the length of time for bubble sort and insertion sort
    """
    sizes = [] # empty list to store values of x
    y_bubble = []
    y_insert = []

    for list_size in range(1000, 10000 + 1, 1000):
        ran_num = []
        for i in range(list_size):
            ran_num.append(random.randint(1, 10000))
        copy_ran_num = list(ran_num)

        # begin timing
        time_bubble = bubble(ran_num)
        y_bubble.append(time_bubble)

        time_insert = insert(copy_ran_num)
        y_insert.append(time_insert)

        sizes.append(list_size)

    # plotting
    pyplot.plot(sizes, y_bubble, 'ro--', label="bubble sort", linewidth=2)
    pyplot.plot(sizes, y_insert, 'go--', label="insertion sort", linewidth=2)
    pyplot.xlabel("number of elements being sorted")
    pyplot.ylabel("time [s]")
    pyplot.legend()
    pyplot.show()

# TESTING
compare_sorts(bubble_sort, insertion_sort)
