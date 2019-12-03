import unittest
from BinarySearch import Binary_Search


class MyTestCase(unittest.TestCase):
    def test_Bi_Search(self):
        self.assertEqual(Binary_Search([2, 3, 4, 5, 6, 7], 0, 5, 4), 2)


if __name__ == '__main__':
    unittest.main()
