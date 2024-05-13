# 데이터가 10000개 ==> O(n^2)까지 가능

import sys


# 그래프를 만든다.
def create_graph(n, m):
    graph = {}

    for i in range(m):  # m
        n1, n2 = map(int, sys.stdin.readline().split())
        if n1 not in graph:
            graph[n1] = []
        if n2 not in graph:
            graph[n2] = []
        graph[n1].append(n2)
        graph[n2].append(n1)

    # 이 때 간선을 정점의 번호 오름차순으로 정렬한다.
    for nodes in graph.values():  # n * klogk
        nodes.sort()

    return graph


def dfs(graph, v):
    visited = set()

    stack = [v]

    ans = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        ans.append(str(node))

        if node not in graph:
            continue

        for i in range(len(graph[node]) - 1, -1, -1):
            if graph[node][i] not in visited:
                stack.append(graph[node][i])

    print(' '.join(ans))
    return ans


def bfs(graph, v):
    visited = set()

    queue = [v]
    visited.add(v)

    ans = []
    while queue:
        node = queue.pop(0)
        ans.append(str(node))

        if node not in graph:
            continue

        for n in graph[node]:
            if n not in visited:
                queue.append(n)
                visited.add(n)

    print(' '.join(ans))


# 정점의 갯수 n, 간선의 갯수 m, 탐색을 시작할 정점의 번호 v를 입력받는다.
n, m, v = map(int, sys.stdin.readline().split())
graph = create_graph(n, m)

# n, m, v = 4, 5, 1
# graph = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

# n, m, v = 5, 5, 3
# graph = [[], [2, 3], [1, 5], [1, 4], [3, 5], [2, 4]]

# n, m, v = 1000, 1, 1000
# graph = {999: [1000], 1000: [999]}
# 정점 v부터 dfs
dfs(graph, v)

# 정점 v부터 bfs
bfs(graph, v)
