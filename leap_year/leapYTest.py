import unittest
from leapYear import leap_year
class TestLeapCase(unittest.TestCase):
    def test_return(self):
        self.assertEqual(leap_year(2014),False)
        self.assertEqual(leap_year(2016), True)
        self.assertEqual(leap_year(400), False)
        self.assertEqual(leap_year(6), False)

if __name__ == '__main__':
    unittest.main()


