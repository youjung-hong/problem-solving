# arr = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

# def sort(e):
#     return e[1]
# arr.sort(key=sort)

# # arr = [(0, 6), (1, 4), (2, 13), (3, 5), (3, 8), (5, 7), (5, 9), (6, 10), (8, 11), (8, 12), (12, 14)]
# arr = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
# print(arr)

import sys

n = int(input())
meetings = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append([start, end])

meetings.sort(key=lambda item: (item[1], item[0]))

t = 0
i = 0
cnt = 0
while i < n:
    if meetings[i][0] >= t:
        cnt += 1
        t = meetings[i][1]
    i += 1

print(cnt)



2 2
3 3
2 3
1 3

2 2
1 3
2 3
3 3