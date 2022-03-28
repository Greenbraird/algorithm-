a = input()
li = [None]*26
ar = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(ar)):
    for j in range(len(a)):
        if li[i]==None and ar[i] == a[j]:
            li[i] = j
    if li[i] == None:
        li[i] = -1
print(' '.join(list(map(str,li))))
