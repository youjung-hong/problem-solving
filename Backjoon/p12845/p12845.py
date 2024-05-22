import sys

n = int(input())

cards = list(map(int, sys.stdin.readline().split()))

cards.sort(reverse=True)

gold = 0
for i in range(1, n):
    gold += (cards[0] + cards[i])

print(gold)
