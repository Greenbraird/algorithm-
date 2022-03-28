
def lenEven(N):
    a = len(N) // 2
    first = N[:a]
    end = N[a:]
    if first == end[::-1]:return "yes"
    else: return 'no'
def lenodd(N):
    a = len(N) // 2
    first = N[:a]
    end = N[a+1:]
    if first == end[::-1]:return "yes"
    else: return 'no'

while True:
    N = input()
    if int(N) == 0:
        break
    elif len(N) %2 == 0:
        print(lenEven(N))
    elif len(N) %2 != 0:
        print(lenodd(N))
        
