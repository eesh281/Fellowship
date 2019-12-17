#*********************************************************************************************************
#@purpose    :to print table of power of 2
#@file name  :power2.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#importing unittest module
import unittest
#importing prime_factor import prime_factor_
from prime_factor import prime_factor_

#creating a test case class
class MyTestCase(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(prime_factor_( 16 ), [ 2,2,2,2 ])
        self.assertEqual(prime_factor_( 8 ), [ 2,2,2 ])
        self.assertEqual(prime_factor_( -8 ), [] )
        self.assertEqual(prime_factor_( -28 ), [] )

#to check whether the module is being imported or not 
if __name__ == '__main__':
    unittest.main()
