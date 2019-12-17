import unittest
from Quadratic import Quadratic1

class MyTestCase(unittest.TestCase):
    def test_Quad(self):
        self.assertTupleEqual(Quadratic1(5,6,3),((-15+12.24744871391589j),(-15-12.24744871391589j)))
        self.assertTupleEqual(Quadratic1(-9,-6,4),(-87.37383539249433, 33.37383539249433))
        self.assertTupleEqual(Quadratic1(-9,-2,-1),(-9.000000000000002-25.455844122715714j,-8.999999999999998+25.455844122715714j))

if __name__ == '__main__':
    unittest.main()
