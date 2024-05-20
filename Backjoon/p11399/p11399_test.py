import unittest

from Backjoon.p11399.p11399 import find_min_time


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        
        self.assertEqual(32, find_min_time([3, 1, 4, 3, 2]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
