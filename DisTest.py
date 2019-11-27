import unittest
from Distance import distance


class MyTestCase(unittest.TestCase):
    def test_dis(self):
        self.assertEqual(distance(6,8),10.0)
        self.assertEqual(distance(2, 4),4.47213595499958)
        self.assertEqual(distance(-6, -4),7.211102550927978)
        self.assertEqual(distance(-5, 7),8.602325267042627)
        self.assertEqual(distance(0, 6),6.0)
if __name__ == '__main__':
    unittest.main()
