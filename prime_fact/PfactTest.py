import unittest
from Pfactors import Prime_Factor

class MyTestCase(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(Prime_Factor(16),[2,2,2,2])
        self.assertEqual(Prime_Factor(8),[2,2,2])
        self.assertEqual(Prime_Factor(-8),[])
        self.assertEqual(Prime_Factor(-28),[])


if __name__ == '__main__':
    unittest.main()
