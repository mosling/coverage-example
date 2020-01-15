import unittest
from adder import add

class AdderTest(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(add(8,8), 16)

if __name__ == "__main__": 
    unittest.main()
