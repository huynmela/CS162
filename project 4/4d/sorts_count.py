# Author: Melanie Huynh
# Date: 27 January 2021
# Description: This program counts number of comparisons and exchanges made while
# sorting a list, returning a tupe of two values (comparisons and exchanges) using
# both bubble sort and insertion count

def bubble_count(a_list):
    """
    This function utilizes a bubble sort method to sort a list while counting
    comparisons and exchanges.
    """
    n = len(a_list)
    swaps = 0 # initializes the counter
    comparisons = 0 # initializes the counter

    for i in range(n):
        for j in range(0, n-i-1):
            if a_list[j] > a_list[j+1]: # comparison made, count
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j] # swap tuple positions
                # count swap and comparison
                swaps += 1
                comparisons += 1
            else:
                comparisons += 1
    return (swaps, comparisons)

def insertion_count(a_list):
    """
    This function utilizes an insertion sort method to sort a list while counting
    comparisons and exchanges.
    """
    swaps = 0 # initializes the counter
    comparisons = 0 # initializes the counter

    for i in range(1, len(a_list)):
        temp = a_list[i]
        j = i - 1
        while j >= 0:
            if temp < a_list[j]:
                comparisons += 1
                a_list[j+1] = a_list[j]
                swaps += 1
                j -= 1
            else:
                comparisons += 1
                break # exist the for-loop as a swap was not able to occur
        a_list[j+1] = temp

    return (swaps, comparisons)

#a = [2, 4, 6, 1, 5, 3]
#print("This is the original list")
#print(a)

#print("This is bubble sort list")
#bubble_count(a)
#print(a)
#print("This is the swap and comparison count from bubble sort")
#print(bubble_count(a))

#a = [2, 4, 6, 1, 5, 3]
#print("This is the original list")
#print(a)

#print("This is the insertion list")
#insertion_count(a)
#print(a)
#print("This is the swap and comparison count from insertion sort")
#print(insertion_count(a))
