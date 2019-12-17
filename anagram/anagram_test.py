#*********************************************************************************************************
#@purpose    :test case of a program to check for anagram
#@file name  :anagram_test.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#importing unittest module
import unittest
#importing anagram from anagram_
from anagram_ import anagram

#creating a class for test case
class MyTestCase(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagram('abcd','bcda'))

#to check whether the module is being imported or not 
if __name__ == '__main__':
    unittest.main()
