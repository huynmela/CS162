# Author: Melanie Huynh
# Date: 3 February 2021
# Description: This program exhaustively searches a .json file containing Nobel Peace
# Prize winners and returns the surnames of the winners in a desired year and category

import json

class NobelData:
    """
    Represents the NobelData object which reads in a .json file containing information
    on all Nobel Peace prize winners in their category and year won.
    """
    def __init__(self):
        """
        Initializes the NobelData object and reads in the .json file
        """
        with open('nobels.json', 'r') as infile:
            self._nobels = json.load(infile)

    def search_nobel(self, year, category):
        """
        Method that takes in a year and category and returns a sorted list of the
         surnames for the winner(s) in that category for that year. Note that the
         year is a string and the categories are "chemistry", "economics", "literature",
         "peace", "physics", and "medicine".
        """
        laureates = [] # stores the laureates
        # exhaustive linear search of the laureates
        for i in range(0, len(self._nobels["prizes"])): # begin at first prize winner
            if self._nobels["prizes"][i]["year"] == year and self._nobels["prizes"][i]["category"] == category:
                laureates = self._nobels["prizes"][i]["laureates"]

        surnames = [] # stores the winners' surnames
        for i in range(0, len(laureates)):
            # extract the surname and append to the list of surnames
            surnames.append(laureates[i]["surname"])

        surnames.sort() # sorts the surnames into normal English dictionary order

        return surnames

# Testing
#nd = NobelData()
#result = nd.search_nobel("1901", "medicine")

#print(result)
