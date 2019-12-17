#*********************************************************************************************************
#@purpose    :test case of a program to perform binary search
#@file name  :binary_test.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#importing unittest module
import unittest
#importing binary_search_ from binary_search
from binary_search import binary_search_

#creating a class for test case
class MyTestCase(unittest.TestCase):
    def test_Bi_Search(self):
        self.assertEqual(binary_search_([2, 3, 4, 5, 6, 7], 0, 5, 4), 2)

#to check whether the module is being imported or not
if __name__ == '__main__':
    unittest.main()
