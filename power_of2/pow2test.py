#*********************************************************************************************************
#@purpose    :test case of a program to print table of power of 2
#@file name  :pow2test.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#importing unittest module
import unittest
#importing power_of_2 from power2.py
from power2 import power_of_2

#creating a test case class
class MyTestCase( unittest.TestCase ):
    def test_pow2( self ):
        self.assertListEqual( power_of_2( 6 ), [ 1, 2, 4, 8, 16, 32, 64 ])
        self.assertListEqual( power_of_2( 2 ), [ 1, 2, 4 ])
        self.assertListEqual( power_of_2( 0 ), [ 1 ])

#to check whether the module is being imported or not 
if __name__ == '__main__':
    unittest.main()
