import unittest

from Backjoon.p1697.p1697_solution import bfs


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(4, bfs(5, 17))  # add assertion here

    def test_case1(self):
        self.assertEqual(4, bfs(5, 17))  # add assertion here


if __name__ == '__main__':
    unittest.main()
