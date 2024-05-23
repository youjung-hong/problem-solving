import sys

n, k = map(int, sys.stdin.readline().split())

coins = []
for i in range(n): # O(n)
    coin = int(input())
    if coin <= k:
        coins.append(coin)

remains = k;
i = len(coins) - 1
count = 0
while remains > 0 and i >= 0:
    if remains >= coins[i]:
        count += int(remains / coins[i])
        remains = int(remains % coins[i])
    else:
        i -= 1

print(count)