import sys
num = int(sys.stdin.readline())
for _ in range(num):
    print(' '.join([i[::-1] for i in list(map(str,sys.stdin.readline().split()))]))

