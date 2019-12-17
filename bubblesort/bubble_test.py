#*********************************************************************************************************
#@purpose    :test case of a program to perform bubble sort
#@file name  :binary_test.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#importing unittest module
import unittest
#importing bubble_sort_ from bubble_sort
from bubble_sort import bubble_sort_

#creating a class for test case
class MyTestCase(unittest.TestCase):
    def test_bub_sort(self):
        self.assertEqual(bubble_sort_([ 76, 23, 1, 6, 8, 56 ]) , [1, 6, 8, 23, 56, 76 ])

#to check whether the module is being imported or not
if __name__ == '__main__':
    unittest.main()
