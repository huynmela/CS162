# Author: Melanie Huynh
# Date: 3 February 2021
# Description: This program takes a text file with a list of numbers and sums the values,
# writing that number to a text file.

def file_sum(text_file):
    """
    Reads in a file with a list of numbers and writes a text file containing the sum
    """
    sum_numbers = 0
    with open(text_file, 'r') as infile:
        for number in infile: # reads each number in each line
            sum_numbers += float(number.strip()) # casts string as float, strips \n

    with open('sum.txt', 'w') as outfile:
        outfile.write(str(sum_numbers)) # must cast float back to string to write

#text_file = 'list_of_numbers.txt'
#file_sum('list_of_numbers.txt')
