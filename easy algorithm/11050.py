N, K = map(int,input().split())
deno = 1; mole = 1
for i in range(K):
    mole *= N; N -= 1 
    deno *= K; K -= 1
print(int(mole/deno))