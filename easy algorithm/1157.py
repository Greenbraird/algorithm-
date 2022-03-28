a = input().upper();li = [0]*26; ma_st = '';ma_in = 0
ar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(ar)):
    for j in range(len(a)):
        if ar[i] == a[j]:
            li[i] += 1
ma_st = ar[li.index(max(li))]; ma_in = max(li); li.remove(max(li))
if ma_in == max(li):
    print('?')
else:
    print(ma_st)