"""
- 노드의 갯수 n과 간선의 갯수 m을 입력 받는다.
- 간선의 갯수 m 만큼 간선목록(u, v)을 입력받고
    - 입력받은 정보로 그래프의 연결 구조를 만든다.
- 노드의 갯수 n 만큼 visited 배열을 만든다.
- 노드의 갯수 n 만큼 순회하면서
    - 노드를 방문하지 않았으면 dfs, for loop 방식으로 방문한다.
        - 방문할 때는 visited 값을 방문했다고 표시
    - 그룹의 갯수를 +1한다.
- 그룹의 갯수를 반환한다.
"""
import sys


def create_graph(m):
    graph = {}
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        if v not in graph:
            graph[v] = []
        graph[v].append(u)

    return graph


def dfs(graph, start, visited):
    stack = [start]
    visited.add(start)

    while stack:
        node = stack.pop()

        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                stack.append(n)


def solution(n, graph):
    visited = set()
    count = 0
    for i in range(1, n+1):
        if i not in graph:
            count += 1
        elif i not in visited:
            dfs(graph, i, visited)
            count += 1

    return count


a, b = map(int, sys.stdin.readline().split())
grp = create_graph(b)

cnt = solution(a, grp)
print(cnt)
