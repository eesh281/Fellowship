import unittest
from BubbleSort import bubble_sort

class MyTestCase(unittest.TestCase):
    def test_bub_sort(self):
        self.assertEqual(bubble_sort([76,23,1,6,8,56]),[1,6,8,23,56,76])


if __name__ == '__main__':
    unittest.main()
