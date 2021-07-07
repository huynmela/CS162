# Author: Melanie Huynh
# Date: 6 January 2021
# Description: This program takes the age of objects Person and calculates the mean, median, and mode of all the ages.

import statistics as stats # imports the module statistics, shortened to stats

class Person:
    """
    Represents a Person object containing methods for getting their name and age.
    """

    def __init__(self, name, age):
        """Returns a Person object with given name and age"""
        self._name = name
        self._age = age

    def get_age(self):
        """Returns the age of the Person object."""
        return self._age

def basic_stats(people):
    """Returns the mean, median, and mode of a list of Person"""
    ages = [] # empty list

    for i in range(0, len(people)):
        ages.append(people[i].get_age()) # Collects all ages into a list

    mean = stats.mean(ages) # Calculates the mean of the ages
    median = stats.median(ages) # Calculates the median of the ages
    mode = stats.mode(ages) # Calculates the mode of the ages

    return mean, median, mode # Returns a tuple of the mean, median, and mode

## Testing
#p1 = Person("Kyoungmin", 73)
#p2 = Person("Mercedes", 24)
#p3 = Person("Avanika", 48)
#p4 = Person("Marta", 24)

#person_list = [p1, p2, p3, p4]
#print(basic_stats(person_list))  # should print a tuple of three values
