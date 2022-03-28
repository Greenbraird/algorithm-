a = int(input());li = [];
for i in range(a):li.append(input())
lis = list(set(li));lis.sort();lis.sort(key=len);
for j in lis:print(j)