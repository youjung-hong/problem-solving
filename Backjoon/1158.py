N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]    # 맨 처음에 원에 앉아있는 사람들

answer = []   # 제거된 사람들을 넣을 배열
i = 0  # 제거될 사람의 인덱스 번호

while len(arr):
    i += K-1  
    i %= len(arr)   # circular로 돌게
    answer.append(str(arr.pop(i)))
print("<",", ".join(answer)[:],">", sep='')