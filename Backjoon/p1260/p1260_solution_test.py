import unittest
from Backjoon.p1260.p1260_solution import bfs, dfs

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_case1(self):
        graph = {
            1: [2, 3, 4],
            2: [1, 4],
            3: [1, 4],
            4: [1, 2, 3]
        }
        self.assertEqual(['1', '2', '4', '3'], dfs(graph, 1))
        self.assertEqual(['1', '2', '3', '4'], bfs(graph, 1))

    def test_case2(self):
        graph = {
            1: [2, 3],
            2: [1, 5],
            3: [1, 4],
            4: [3, 5],
            5: [2, 4]
        }
        self.assertEqual(['3', '1', '2', '5', '4'], dfs(graph, 3))
        self.assertEqual(['3', '1', '4', '2', '5'], bfs(graph, 3))

    def test_case3(self):
        graph = {
            999: [1000],
            1000: [999]
        }
        self.assertEqual(['1000', '999'], dfs(graph, 1000))
        self.assertEqual(['1000', '999'], bfs(graph, 1000))

    def test_case4(self):
        graph = {
            1: [3, 4]
        }
        self.assertEqual(['2'], dfs(graph, 2))
        self.assertEqual(['2'], bfs(graph, 2))


if __name__ == '__main__':
    unittest.main()
