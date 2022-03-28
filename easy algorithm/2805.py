import sys
input = sys.stdin.readline

N, M = map(int,input().split()) # 나무 수, 필요한 나무 길이
trees = list(map(int, input().split()))

start, end = 0, max(trees) # 시작 점, 끝점

# 이분 탐색
while start <= end:
    mid = (start+end)//2
    tree = 0 
    for i in trees:
        if i > mid: 
            tree += i - mid

    if tree >= M:
        start = mid + 1
    else: 
        end = mid - 1
print(end)