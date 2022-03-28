import sys
li = [0 for _ in range(10001)]

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    li[num] += 1
for i in range(1, 10001):
    count = li[i]
    for _ in range(count):
        print(i)
