T = int(input())

for i in range(T):
    ho = 1
    H, W, N = map(int, input().split())
    while H < N:
        N -= H
        ho += 1
    print(N*100 + ho)
