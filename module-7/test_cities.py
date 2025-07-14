# Mikaela Snell
# CSD-325
# Module 7 Assignment 7.2: City Functions Unittest
# This program tests the city_functions.py program using unittest following instructions from Chapter 11 - Testing Your Code Python Crash Course: A Hands-On, Project-Based Introduction to Programming, 2nd Edition by  Eric Matthes No Starch Press © 2019 Citation
# 7/13/2025

import unittest
from city_functions import city_country

class CitiesTest(unittest.TestCase):
    """Tests 'city_functions.py'"""

    def test_city_country(self):
        formatted_location = city_country("santiago", "chile")
        self.assertEqual(formatted_location, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
