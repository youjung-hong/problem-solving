def find_max_cut_height(trees, m):
    low = 1
    high = max(trees)

    # 원하는 길이가 나올 때까지 이진 탐색
    ans = high
    while high >= low:
        mid = (low + high) // 2
        # 자를 수 있는 나무 길이를 구한다
        h = 0
        for t in trees:
            if t > mid:
                h = h + t - mid
            if h >= m:
                break
        if h >= m:  # 더 길거나 똑같이 자름 -> 더 짧게 자를 수 있게 중심을 높여야 함 
            low = mid + 1
        else:  # 더 짧게 자름 -> 더 길게 자를 수 있게 중심을 낮춰야 함 
            high = mid - 1

    print(high)


# 입력
n, m = map(int, input().split())
trees = list(map(int, input().split()))
find_max_cut_height(trees, m)
