# Author: Melanie Huynh
# Date: 13 January 2021
# Description: This program is a tester which contains 5 different unit tests for Store.py

import unittest

class TestStore(unittest.TestCase):
    """
    Defines unit tests for the
    """

    def test_1(self):
        """
        Test Member 1: Purchasing one item with a preimium membership
        """
        p_1 = Product("435", "dog", "wags its tail when happy", 600.52, 1)
        c_1 = Customer("Faaiq", "541", True)
        myStore = Store()

        myStore.add_product(p_1)
        myStore.add_member(c_1)
        myStore.add_product_to_member_cart(p_1.get_product_id, c_1.get_customer_id)
        result = myStore.check_out_member(c_1.get_customer_id)

        self.assertEqual(result, 600.52)

    def test_2(self):
        """
        Test Member 2: Attempting to purchase an item that has no quanity availabile
        """
        p_1 = Product("ab42", "Chipotle", "a tasty fast food", 8.60, 0)
        c_1 = Customer("Kendra", "perki10", False)
        myStore = Store()

        myStore.add_product(p_1)
        myStore.add_member(c_1)
        myStore.add_product_to_member_cart(p_1.get_product_id, c_1.get_customer_id)
        result = myStore.check_out_member(c_1.get_customer_id)

        self.assertEqual(result, 0)

    def test_3(self):
        """
        Test Member 3: Checking to see if a product is in inventory
        """
        p_1 = Product("707LOL", "tetris", "building blocks", 5.75, 10)
        myStore = Store()
        result = myStore.product_search("tetris")

        assertIn("tetris", result)

    def test_4(self):
        """
        Test Member 4: Attempting to purchase an item without premium shipping
        """
        p_1 = Product("1800cleaner", "bone", "the skeleton of an animal", 10.50, 3)
        c_1 = Customer("sushi", "d0gz", False)
        myStore = Store()

        myStore.add_product(p_1)
        myStore.add_member(c_1)
        myStore.add_product_to_member_cart(p_1.get_product_id, c_1.get_customer_id)
        result = myStore.check_out_member(c_1.get_customer_id)

        self.assertNotEqual(result, 10.50)

    def test_5(self):
        """
        Test Member 5: Checks to see if the shipping cost is added when member is
        not premium
        """
        p_1 = Product("8413", "Leg", "bottom body part", 8.75, 10)
        p_2 = Product("600", "Arm", "upper body part", 8.75, 10)
        c_1 = Customer("Mel", "rnela", False)

        myStore = Store()
        myStore.add_product(p_1)
        myStore.add_product(p_2)
        myStore.add_member(c_1)

        myStore.add_product_to_member_cart(p_1.get_product_id, c_1.get_customer_id)
        result = myStore.check_out_member(c_1.get_customer_id)

        assertAlmostEqual(result, 21.44, 1)

if __name__ == '__main__':
    unittest.main()
