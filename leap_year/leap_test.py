#*********************************************************************************************************
#@purpose    :test case of a program to determine whether an year is leap or not
#@file name  :leap_test.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#importing unittest module
import unittest
#importing 
from leap_year1 import leap_year

#creating a test case class
class TestLeapCase(unittest.TestCase):

    def test_return(self):
        self.assertEqual( leap_year( 2014 ), False)
        self.assertEqual( leap_year( 2016 ), True)
        self.assertEqual( leap_year( 400 ), False)
        self.assertEqual( leap_year( 6 ), False)

#to check whether the module is being imported or not 
if __name__ == '__main__':
    unittest.main()


