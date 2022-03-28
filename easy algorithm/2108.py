from collections import Counter
import sys
a = int(sys.stdin.readline())
li = []
for i in range(a):
    li.append(int(sys.stdin.readline()))
#산술평균
print(round(sum(li)/len(li)))
#중앙값
li.sort()
print(li[len(li)//2])
#최빈값
mode_dict = Counter(li)
modes = mode_dict.most_common()    
    
if len(li) > 1 : 
    if modes[0][1] == modes[1][1]:
        print(modes[1][0])
    else: 
        print(modes[0][0])
else: 
        print(modes[0][0])
#범위
print(max(li)-min(li))
