#*********************************************************************************************************
#@purpose    : test case of a program to calcute distance between to origin from two points x,y
#@file name  :dis_test.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#importing unittest module
import unittest
#importing distance method from distance.py
from distance import distance_

#creating a test case class
class MyTestCase(unittest.TestCase):
    def test_dis(self):
        self.assertEqual(distance_( 6, 8 ), 10.0 )
        self.assertEqual(distance_( 2, 4 ), 4.47213595499958 )
        self.assertEqual(distance_( -6, -4 ), 7.211102550927978 )
        self.assertEqual(distance_( -5, 7 ), 8.602325267042627 )
        self.assertEqual(distance_( 0, 6 ) , 6.0 )

#to check whether the module is being imported or not 
if __name__ == '__main__':
    unittest.main()
