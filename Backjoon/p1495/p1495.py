"""
- 볼륨 목록 = set(시작볼륨 S)
- n 만큼 반복하면서
    - 새 볼륨목록 = set()
    - 볼륨 목록에서 + V[i] ≤ M이면, 새 볼륨목록에 추가
    - 볼륨 목록에서 - V[i] ≥ 0이면, 새 볼륨목록에 추가
    - 볼륨 목록 교체
- 볼륨 목록의 최댓값 구하기
"""
import sys
n, s, m = map(int, sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))

cur_v = set()
cur_v.add(s)
for i in range(n):
    new_v = set()
    for vv in cur_v:
        print
        if vv + v[i] <= m:
            new_v.add(vv + v[i])
        if vv - v[i] >= 0:
            new_v.add(vv - v[i])
    cur_v = new_v

if len(cur_v):
    print(max(cur_v))
else:
    print(-1)