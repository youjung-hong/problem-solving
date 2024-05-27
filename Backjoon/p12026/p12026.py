import sys

n = int(input())
road = sys.stdin.readline().strip()

power = 0
boj = ['B', 'O', 'J']
boj_i = 1
prev = 0
ans = False
for i in range(1, len(road)):
    if road[i] == boj[boj_i]:
        power += pow(i - prev, 2)
        prev = i
        boj_i = (boj_i + 1) % 3
        if i == len(road) - 1:
            ans = True

if ans:
    print(power)
else:
    print(-1)