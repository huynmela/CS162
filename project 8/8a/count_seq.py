# Author: Melanie Huynh
# Date: 2/24/2021
# Description: A generator function producing a "look and say" sequence

def iterating_num(seq):
    """
    A sort of 'helper function' to assist in count_seq as it requires an input sequence to run
    """
    result = "" # will store resulting sequence
    temp_list = [] # temp list while stores sequence
    i = 0 # keeps track of how many times a certain number has been encountered
    # ensure you are still within the bounds of the string sequence
    while i < len(seq): # while the iterator is less than the length of the string of the sequence
        # now that you've entered the loop, you keep track of how many times to same number appears
        counter = 1 # the first number appears once
        # there are two parameters to keep track of, knowing you are within the
        # bounds and if the next number in the sequence is the same as the one you're on.
        while i + 1 < len(seq) and seq[i] == seq[i + 1]:
            # move onto the next and mutate i and counter
            counter += 1 # means you've come across the same number again
            i += 1 # means you've can move on to the next one
        temp_list.append(str(counter) + seq[i]) # append the sequence to the results
        i += 1 # move to next iteration
    return result.join(temp_list)

def count_seq():
    """
    Generator function generating a look and say sequence begining with 2
    """
    # define the first number to enter the while loop
    n = 1
    # then enter the while loop
    while True:
        # define special cases
        if n == 1:
            n += 1
            yield "2" # begin with 2 for the case
        elif n == 2: # move onto next case
            n += 1
            num = "12"
            yield num
        else: # then go on into the rest of the cases
            # begin at the second case
            result = iterating_num(num)
            yield result
            num = result
# TESTING
#result = count_seq()

#for res in result:
#    print(res)
