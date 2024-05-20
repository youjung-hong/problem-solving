import sys


def find_min_time(arr):
    arr.sort()

    sum = 0
    for i in range(n):
        sum += arr[i]*(n-i)

    return sum

n = int(input())

arr = map(int, sys.stdin.readline().split())
sum = find_min_time(arr)
