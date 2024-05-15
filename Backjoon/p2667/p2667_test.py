import unittest

from Backjoon.p2667.p2667 import find_group, split


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        arr = [
            '0110100',
            '0110101',
            '1110101',
            '0000111',
            '0100000',
            '0111110',
            '0111000'
        ]
        arr = split(arr)
        self.assertEqual([7, 8, 9], find_group(arr))  # add assertion here


if __name__ == '__main__':
    unittest.main()
