#*********************************************************************************************************
#@purpose    :test case of a program to perform insertion sort
#@file name  :insertion_test.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#importing unittest module
import unittest
#importing insertion_sort_ from insertion_sort
from insertion_sort import insertion_sort_

#creating a class for test case
class MyTestCase(unittest.TestCase):
    def test_ins_sort(self):
        self.assertEqual(insertion_sort_([ 2, 4, 6, 3, 1, 7 ]), [ 1, 2, 3, 4, 6, 7 ])

#to check whether the module is being imported or not
if __name__ == '__main__':
    unittest.main()
