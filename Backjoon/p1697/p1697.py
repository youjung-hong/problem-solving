"""
- 노드 N에서 bfs로 K에 도달하는 방법을 찾는다.
    - n == k: return 0
    - 큐에 (N, 0)을 넣는다.
    - 큐에 값이 있을 때까지 반복
        - (x, cnt) = queue.pop(0)
        - x = x - 1, x + 1, 2x 를 방문
            - x == k 이면, return cnt+1
            - 0 ≤ x ≤ 100,000 이면, queue.append((x, cnt+1))
"""

def bfs(n, k):
    if n == k:
        return 0

    queue = [(n, 0)]
    visited = set()
    visited.add(n)

    while queue:
        (x, cnt) = queue.pop(0)

        a = x - 1
        b = x + 1
        c = 2*x

        if a == k or b == k or c == k:
            return cnt + 1
        if 0 <= a <= 100000 and a not in visited:
            visited.add(a)
            queue.append((a, cnt+1))
        if 0 <= b <= 100000 and b not in visited:
            visited.add(b)
            queue.append((b, cnt+1))
        if 0 <= c <= 100000 and c not in visited:
            visited.add(c)
            queue.append((c, cnt+1))

    return -1


n, k = map(int, input().split())

cnt = bfs(n, k)
print(cnt)