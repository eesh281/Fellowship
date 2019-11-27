import unittest
from power2 import power_of_2

class MyTestCase(unittest.TestCase):
    def test_pow2(self):
        self.assertListEqual(power_of_2(6),[1,2,4,8,16,32,64] )
        self.assertListEqual(power_of_2(2),[1,2,4] )
        self.assertListEqual(power_of_2(0),[1] )
       # self.assertListEqual(power_of_2(-1),[0.5] )


if __name__ == '__main__':
    unittest.main()
