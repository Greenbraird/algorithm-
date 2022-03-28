N, K = map(int, input().split())
K -= 1
number = K
N_lst = []
lst = list(range(1,N+1))
while len(lst) > 0:
    while len(lst) <= number:
        number -= len(lst)
    N_lst.append(lst.pop(number))
    number += K
print(str(N_lst).replace('[','<').replace(']','>'))
