import unittest

from Backjoon.p11724.p11724_solution import solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        n, m = 6, 5
        graph = {
            1: [2, 5],
            2: [1, 5],
            5: [2, 1],
            3: [4],
            4: [3, 6],
            6: [4]
        }
        self.assertEqual(2, solution(n, graph))  # add assertion here

    def test_case2(self):
        n, m = 6, 8
        graph = {
            1: [2, 5],
            2: [1, 4, 3],
            5: [1, 4],
            3: [4, 2],
            4: [3, 6, 5, 2],
            6: [4]
        }
        self.assertEqual(1, solution(n, graph))  # add assertion here



if __name__ == '__main__':
    unittest.main()
