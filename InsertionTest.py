import unittest
from InsertionSort import insertion_sort


class MyTestCase(unittest.TestCase):
    def test_ins_sort(self):
        self.assertEqual(insertion_sort([2, 4, 6, 3, 1, 7]), [1, 2, 3, 4, 6, 7])


if __name__ == '__main__':
    unittest.main()
