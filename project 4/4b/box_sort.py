# Author: Melanie Huynh
# Date: 27 January 2021
# Description: This program uses insertion sort to sort a list of Boxes from
# greatest volume to least volume.

class Box:
    """
    Represents a Box oject with given length, width, and height
    """

    def __init__(self, length, width, height):
        """
        Initializes the Box object
        """
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        """
        Returns the volume of the Box object
        """
        return self._length * self._width * self._height

    def get_length(self):
        """
        Returns the length of the Box object
        """
        return self._length

    def get_width(self):
        """
        Returns the width of the Box object
        """
        return self._width

    def get_height(self):
        """
        Returns the height of the Box object
        """
        return self._height

def box_sort(a_list):
    """
    Sorts a_list of Box objects in greatest to least volume
    """

    for i in range(1, len(a_list)):
        temp_object = a_list[i]
        position = i - 1

        while position >= 0 and a_list[position].volume() < temp_object.volume():
            a_list[position + 1] = a_list[position]
            position -= 1

        a_list[position + 1] = temp_object

def main():
    b1 = Box(3.4, 19.8, 2.1)
    b2 = Box(1.0, 1.0, 1.0)
    b3 = Box(8.2, 8.2, 4.5)
    box_list = [b1, b2, b3]
    box_sort(box_list)

if __name__ == '__main__':
    main()

