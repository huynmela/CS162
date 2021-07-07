# Author: Melanie Huynh
# Date: 13 January 2021
# Description: This program is a simulation of a store which allows a customer to add products into their cart and check out items listed in the store's inventory.

class Product:
    """
    Represents a Product object containing methods for its title, ID, description,
    price, and quantity available.
    """

    def __init__(self, product_id, title, description, price, quantity_available):
        """
        Returns a Product object with given product ID, title, description,
        price, and the quantity available.
        """
        self._product_id = product_id
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_product_id(self):
        """
        Returns the product ID of the Product object
        """
        return self._product_id

    def get_title(self):
        """
        Returns the title of the Product object
        """
        return self._title

    def get_description(self):
        """
        Returns the descritpion of the Product object
        """
        return self._description

    def get_price(self):
        """
        Returns the price of the Product object
        """
        return self._price

    def get_quantity_available(self):
        """
        Returns the quantity available of the Product object
        """
        return self._quantity_available

    def decrease_quantity(self):
        """
        Decreases the quantity of product available by one
        """
        self._quantity_available -= 1

class Customer:
    """
    Represents a Customer object containing methods for getting their
    """

    def __init__(self, name, customer_id, premium_member):
        """
        Returns a Customer object with given name, id, and whether they are a
        premium member or not
        """
        self._name = name
        self._customer_id = customer_id
        self._premium_member = premium_member
        self._customer_cart = [] # initializes an empty list representing an empty cart

    def get_customer_cart(self):
        """
        Returns Customer object cart
        """
        return self._customer_cart

    def get_name(self):
        """
        Returns Customer object name
        """
        return self._name

    def get_customer_id(self):
        """
        Returns Customer object id
        """
        return self._customer_id

    def is_premium_member(self):
        """
        Returns whether the customer is a premium member
        """
        return self._premium_member

    def add_product_to_cart(self, product_id):
        """
        Takes a product ID code and adds it to the Customer's cart
        """
        return self._customer_cart.append(product_id)

    def empty_cart(self):
        """
        Empties the Customer's cart
        """
        self._customer_cart = []

class Store:
    """
    Represents a store which has some number of products in its inventory and
    number of customers as members
    """

    def __init__(self, inventory, membership_list):
        """
        Returns a Store object with inventory and a membership list
        """
        self._inventory = [] # initializes an empty list representing an empty inventory
        self._membership_list = [] # initializes an empty list as an empty  membership list

    def add_product(self, product):
        """
        Takes a Product object and adds it to the inventory
        """
        return self._inventory.append(product)

    def add_member(self, member):
        """
        Takes a Customer object and adds it to the membership
        """
        return self._membership_list.append(member)

    def get_product_from_id(self, prod_id):
        """
        Takes a Product object ID and returns the Product with the matching ID.
        If no matching ID is found in the inventory, it returns None
        """
        result = 0 # will be redefined by the result from the for-loop and returned

        for prod in self._inventory:
            if prod.get_product_id() == prod_id:
                result = prod
            else:
                result = None
        return result

    def get_member_from_id(self, cus_id):
        """
        Takes a Customer ID and returns the Customer with the matching ID. If no
        matching ID is found in the membership, it returns None
        """
        result = 0 # will be redefined by the result from the for-loop and returned

        for member in self._membership_list:
            if member.get_customer_id == cus_id:
                result = member
            else:
                result = None
        return result

    def product_search(self, prod_search):
        """
        Takes a search string and returns a sorted list of ID codes for every product
        in the inventory whose title or description contains the search string
        """
        list_search = [] # empty list to fill with products

       # Checking search key in names of products
        for product in self._inventory:
            for prod_letter in product.get_title():

                title_index = 0 # Checking each letter beginning with the first one

                if prod_letter.lower() == prod_search[title_index].lower():
                    title_index += 1 # Adds to the counter
                else:
                    title_index = 0 # Resets the counter

                if title_index == len(prod_search): # Append the product id to the search list
                    list_search.append(product.get_product_id())
        #Checking search key in descriptions of products
            for desc_letter in product.get_description():

                desc_index = 0 # Checking each letter beginning with the first one

                if desc_letter.lower() == prod_search[desc_index].lower():
                    desc_index += 1 # Adds to the counter
                else:
                    desc_index = 0 # Resets the counter

                if desc_index == len(prod_search): # Append the product id to the search list
                    list_search.append(product.get_product_id())

        # Sorting the list in lexicographical order
        sorted(list_search, key=str.lower)

        return set(list_search) # Removing repeated words

    def add_product_to_member_cart(self, prod_id, cus_id):
        """
        Takes a Product ID and a Customer ID, checks to see if the product is available
        and the Customer is an member. If so, the product will be added to the
        Customer's cart
        """
        result = 0 # will be redefined by the result of the if/elif/else below
        customer = self.get_member_from_id(cus_id)
        product = self.get_product_from_id(prod_id)

        # Check if the producct is not in
        if product == None:
            result = "product ID not found"
        # Check if the customer is not in
        elif customer == None:
            result = "member ID not found"
        # add the product to the member cart
        else:
            #check availablity of product
            if product.get_quantity() > 0:
                customer.add_product_to_cart(prod_id)
                result = "product added to cart"
            else:
                result = "product out of stock"

        return result

    def check_out_member(self, cus_id):
        """
        Takes a Customer ID and checks if the ID is a member of the Store. If so,
        a charge will be returned for the member's cart totaling the cost of all
        items in the cart if they are in stock.
        """

        customer = self.get_member_from_id(cus_id) # retrieves customer object from id
        cart_total = 0 # initializes total in cart
        shipping_cost = 0 # initializes shipping cost

        for member in self._membership_list:
            if member.get_customer_id == cus_id: # checks if member

                for product_id in customer.get_customer_cart(customer):

                    for item in self._inventory:

                        if product_id == item.get_product_id():

                            if item.get_quantity_available() > 0:
                                cart_total += product.get_price() # totals product price in cart
                                item.decrease_quantity() # decreases the quantity of product available

                # Check if member is premium
                if customer.is_premium_member() == True:
                    shipping_cost = 0
                else:
                    shipping_cost = 0.07 * cart_total

            else:
                raise InvalidCheckoutError

        customer.empty_cart()
        total = cart_toal + shipping_cost
        return total


class InvalidCheckoutError(Exception):
    """
    An error raised when an ID of a Customer does not match a member of a Store
    during checkout
    """
    pass

def main():
        p1 = Product("123", "Chicken", "a bird called chicken that lays eggs", 4.51, 8)
        c1 = Customer("Joy", "503", True)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart(p1.get_product_id, c1.get_customer_id)

        try:
            result = myStore.check_out_member(c1.get_customer_id)
        except InvalidCheckoutError:
            print("The Customer is not a member of the Store.")

if __name__ == '__main__':
    main()
