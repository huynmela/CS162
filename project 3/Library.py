# Author: Melanie Huynh
# Date: 20 January 2021
# Description: This program is a simulation of a library that allows a user to check out,
# pay fines, and search for items.

class LibraryItem:
    """
    Represents the LibraryItem object which inherits a group of classes (Book, Album,
    and Movie) with general methods for all library items for location, availability,
    requests, and date of check out
    """
    def __init__(self, library_item_id, title):
        """
        Initializes LibraryItem object
        """
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = 0 #
        self._location = "ON_SHELF"

    def get_location(self):
        """
        Returns the location of a LibraryItem object
        """
        return self._location

    # EXTERNAL GET METHODS -------------------------------------------------------
    def get_library_item_id(self):
        """
        Returns the item ID of a LibraryItem object
        """
        return self._library_item_id

    def get_checked_out_by(self):
        """
        Returns the patron that checked out the LibraryItem object
        """
        return self._checked_out_by

    def get_requested_by(self):
        """
        Returns the patron that requested the LibraryItem object
        """
        return self._requested_by

    def get_date_checked_out(self):
        """
        Returns the date the item was checked out
        """
        return self._date_checked_out

    def set_requested_by(self, temp):
        """
        Changes the requested by to another patron
        """
        self._requested_by = temp

    def set_checked_out_by(self, temp):
        """
        Changes the checked_out_by to another patron
        """
        self._checked_out_by = temp

    def set_date_checked_out(self, temp):
        """
        Changes the date_checked_out to the time item was checked out
        """
        self._date_checked_out = temp

    def set_location(self, temp):
        """
        Changes the location of an item
        """
        self._location = temp

# -----------------------------------------------------------------------------
# Subclasses of Library Item Object
# -----------------------------------------------------------------------------

class Book(LibraryItem):
    """
    Represents a Book object, subclass to LibraryItem, that can be checked-out
    for a length of 21 days
    """
    def __init__(self, library_item_id, title, author):
        """
        Initializes Book object
        """
        self._author = author
        super().__init__(library_item_id, title)

    def get_check_out_length(self):
        """
        Returns length of time for checking out Book object
        """
        return 21 # days

    def get_author(self):
        """
        Returns the author of Book object
        """
        return self._author

class Album(LibraryItem):
    """
    Represents an Album object, subclass to LibraryItem, that can be checked-out
    for a length of 14 days
    """
    def __init__(self, library_item_id, title, artist):
        """
        Initializes Album object
        """
        self._artist = artist
        super().__init__(library_item_id, title)

    def get_check_out_length(self):
        """
        Returns the length of time for checking out Album object
        """
        return 14 # days

    def get_artist(self):
        """
        Returns the artist of Album object
        """
        return self._artist

class Movie(LibraryItem):
    """
    Represents a Movie object, subclass to LibraryItem, that can be checked-out
    for a length of 7 days
    """
    def __init__(self, library_item_id, title, director):
        """
        Initializes Movie object
        """
        self._director = director
        super().__init__(library_item_id, title)

    def get_check_out_length(self):
        """
        Returns the length of time for checking out Movie object
        """
        return 7 # days

    def get_director(self):
        """
        Returns the director of Movie object
        """
        return self._director

# ------------------------------------------------------------------------------
# Patron object
# ------------------------------------------------------------------------------

class Patron:
    """
    Represents a Patron object containing methods to check out or return LibraryItems,
    and check fines on the account
    """
    def __init__(self, patron_id, name):
        """
        Initializes Patron object
        """
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = [] # initially empty
        self._fine_amount = 0

    def get_fine_amount(self):
        """
        Returns Patron object's fine amount
        """
        return self._fine_amount

    def add_library_item(self, library_item):
        """
        Adds a library item to Patron's checked out items
        """
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """
        Removes a library item from Patron's checked out items
        """
        self._checked_out_items.remove(library_item)

    def amend_fine(self, fine_charge):
        """
        Changes a fine amount on Patron object
        """

        self._fine_amount += fine_charge

    # TESTING GETS AND SETS ----------------------------------------------------
    def get_patron_id(self):
        """
        Returns the ID of a Patron object
        """
        return self._patron_id

    def get_name(self):
        print(self._name)

    def get_checked_out_items(self):
        """
        Returns a Patron's checked out items
        """
        return self._checked_out_items

# ------------------------------------------------------------------------------
# Library object
# ------------------------------------------------------------------------------

class Library:
    """
    Represents a Library object containing methods to
    """
    def __init__(self):
        """
        Initializes Library object
        """
        self._holdings = []
        self._members = []
        self._current_date = 0

    def add_library_item(self, library_item):
        """
        Adds a LibraryItem object to the holdings
        """
        self._holdings.append(library_item)

    def add_patron(self, patron):
        """
        Adds a Patron object to the list of members
        """
        self._members.append(patron)

    def get_library_item_from_id(self, item_id):
        """
        Returns a LibraryItem Object corresponding to the ID parameter. None is
        returned if no such LibraryItem is in the holdings
        """
        result = 0 # will be redefined by for-loop and returned

        for item in self._holdings:
            if item_id == item.get_library_item_id():
                result = item
            else:
                result = None
        return result

    def get_patron_from_id(self, patron_id):
        """
        Returns a Patron Object corresponding to the ID parameter. None is returned
        if no such Patron is a member
        """
        result = 0 # will be redefined by for-loop and returned

        for member in self._members:
            if patron_id == member.get_patron_id():
                result = member
            else:
                result = None
        return result

    def check_out_library_item(self, patron_id, item_id):
        """
        Checks out a LibraryItem object to a Patron object
        """
        patron = self.get_patron_from_id(patron_id)
        item = self.get_library_item_from_id(item_id)

        # check if the patron is in
        if patron == None:
            return "patron not found"
        # check if the item is in
        elif item == None:
            return "item not found"
        # check item location
        elif item.get_location() == "CHECKED_OUT":
            return "item already checked out"
        elif item.get_location() == "ON_HOLD_SHELF":
            # check to see if the requester is the same as the one passed in
            # if yes, the item's requested_by will be set to None
            if item.set_requested_by.get_patron_id() == patron_id:
                item.set_requested_by(None)
            # if not, the item cannot be checked out by the patron passed in
            else:
                return "item on hold by other patron"
        # otherwise update LibraryItem's checked_out_by, date_checked_out and location
        else:
            item.set_checked_out_by(patron)
            item.set_date_checked_out(self._current_date)
            item.set_location("CHECKED_OUT")

            # then update Patron's checked_out_items
            patron.add_library_item(item)

            return "check out successful"

    def return_library_item(self, item_id):
        """
        Allows for a LibraryItem object to be returned
        """
        item = self.get_library_item_from_id(item_id)
        patron = item.get_checked_out_by()

        # check if item is not in Library's holdings
        if item not in self._holdings:
            return "item not found"
        # check if item is checked not out
        if item.get_location() != "CHECKED_OUT":
            return "item already in library"
        # otherwise, return the item
        # update Patron's checked_out_items
        patron.remove_library_item(item)
        # update item's location depending on if another Patron required it
        if item.get_requested_by() != None: # this would be a Patron if it was requested
            item.set_location("ON_HOLD_SELF") # because it is a Patron, the item is on hold
        # otherwise, the item is returned on the shelf
        else:
            item.set_location("ON_SHELF")
        # update item's checked_out_by
        item.set_checked_out_by(None)
        return "return successful"

    def request_library_item(self, patron_id, item_id):
        """
        Allows for a Patron object to request for a LibraryItem object
        """
        item = self.get_library_item_from_id(item_id)
        patron = self.get_patron_from_id(patron_id)

        # check if patron is not in library's members
        if patron not in self._members:
            return "patron not found"
        # check if item is not in holdings
        if item not in self._holdings:
            return "item not found"
        # ch88.08eck if item is already requested
        if item.get_requested_by() != None: # this would be a Patron if it was requested
            return "item already on hold"
        # update item's requested_by to the patron requesting
        item.set_requested_by(patron)
        # check if item is on shelf
        if item.get_location() == "ON_HOLD_SHELF":
            item.set_location("ON_HOLD")

        return "request successful"

    def pay_fine(self, patron_id, amount):
        """
        Allows for a Patron object to pay their fine
        """
        patron = self.get_patron_from_id(patron_id)

        # checks if patron is not in library's members
        if patron not in self._members:
            return "patron not found"

        # use amend_fine to update patron's fine
        patron.amend_fine(-amount)

        return "payment successful"

    def increment_current_date(self):
        """
        Increases a Patron object's fines by 10 cents for each overdue LibraryItem object
        they have checked out
        """

        self._current_date += 1

        for patron in self._members:
            for item in patron.get_checked_out_items():
                if self._current_date - item.get_date_checked_out() > item.get_check_out_length():
                    patron.amend_fine(0.10)

def main():
    """
    Function for testing
    """
    #test_libitems = []
    #test_books = []
    #test_movies = []
    #test_albums = []
    #test_patrons = []
    #name = "milkbone5"
    #authorz = "sushi69"

    #for i in range(5):
    #    test_libitems.append(LibraryItem(i,name))
    #    test_books.append(Book(str(i+5),name,authorz))
    #    test_movies.append(Movie(str(i+10),name,authorz))
    #    test_albums.append(Album(str(i+15),name,authorz))
    #    test_patrons.append(Patron(str(i+20),name))

    b1 = Book("345", "Bookie", "Rye")
    b2 = Book("456", "Novel", "Davis")
    print(b1.get_author())
    print(b2.get_author())

    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")

    lib = Library()

    lib.add_library_item(b1)
    lib.add_library_item(b2)

    lib.add_patron(p1)
    lib.add_patron(p2)

    lib.check_out_library_item("bcd", "456")
    lib.request_library_item("abc", "456")


    for i in range(57):
        lib.increment_current_date()

    p1_fine = p1.get_fine_amount()
    p2_fine = p2.get_fine_amount()

    lib.pay_fine("abc", p1_fine)
    lib.pay_fine("bcd", p2_fine)

if __name__ == '__main__':
    main()
