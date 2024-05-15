import sys

def bfs(arr, i, j, visited):
    queue = [(i, j)]
    visited[i][j] = 1
    count = 1

    while queue:
        n, m = queue.pop(0)

        # 위
        if n > 0 and arr[n - 1][m] == '1' and visited[n - 1][m] == 0:
            count += 1
            visited[n - 1][m] = 1
            queue.append((n - 1, m))

        # 아래
        if n < len(arr)-1 and arr[n+1][m] == '1' and visited[n+1][m] == 0:
            count += 1
            visited[n+1][m] = 1
            queue.append((n+1, m))

        # 오른쪽
        if m < len(arr) - 1 and arr[n][m + 1] == '1' and visited[n][m + 1] == 0:
            count += 1
            visited[n][m + 1] = 1
            queue.append((n, m + 1))

        # 왼쪽
        if m > 0 and arr[n][m - 1] == '1' and visited[n][m - 1] == 0:
            count += 1
            visited[n][m - 1] = 1
            queue.append((n, m - 1))



    return count

def split(arr1):
    arr2 = []
    for item in arr1:
        arr2.append(list(item))
    return arr2

def find_group(arr):
    n = len(arr)
    visited = [[0 for _ in range(n)] for _ in range(n)]

    ans = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '1' and visited[i][j] == 0:
                num = bfs(arr, i, j, visited)
                ans.append(num)

    ans.sort()
    return ans

arr = []
for i in range(int(sys.stdin.readline())):
    arr.append(list(sys.stdin.readline()))
ans = find_group(arr)

print(len(ans))
for num in ans:
    print(num)