import unittest
from Anagram import anagram

class MyTestCase(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagram('abcd','bcda'))


if __name__ == '__main__':
    unittest.main()
