#*********************************************************************************************************
#@purpose    :test case of a program for solve a quadratic equation
#@file name  :quad_test.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#importing unittest module
import unittest
#importing quadratic1 from quadratic_
from quadratic_ import quadratic1

class MyTestCase(unittest.TestCase):
    def test_Quad(self):
        self.assertTupleEqual( quadratic1( 5,6,3 ), (( -15 + 12.24744871391589j ), ( -15-12.24744871391589j )))
        self.assertTupleEqual( quadratic1( -9,-6,4 ), ( -87.37383539249433, 33.37383539249433 ))
        self.assertTupleEqual( quadratic1( -9,-2,-1 ), ( -9.000000000000002-25.455844122715714j, -8.999999999999998 + 25.455844122715714j ))

#to check whether the module is being imported or not 
if __name__ == '__main__':
    unittest.main()
