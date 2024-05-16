import sys
sys.setrecursionlimit(10**6)

xy = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(graph, i, j, n, m):
    if i < 0 or i == n or j < 0 or j == m:
        return

    if graph[i][j] == 0:
        return

    graph[i][j] = 0

    for item in xy:
        dfs(graph, i + item[0], j + item[1], n, m)


ans = []
t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y, x = map(int, sys.stdin.readline().split())
        arr[x][y] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                count += 1
                dfs(arr, i, j, n, m)

    ans.append(count)

for i in ans:
    print(i)