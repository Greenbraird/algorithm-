from os import rename


N, K = map(int,input().split())

table = [i for i in range(1,N+1)]
ran = []
while len(ran) != N :
    if len(table) < K:
        K = K - N 
    ran.append(table.pop(K-1))
    K += 3
print(ran)
