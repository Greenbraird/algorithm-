import math
a = int(input()); li = []
for i in range(2, a+1):
    while True:
        if  a % i == 0:
            li.append(i)
            a = a/i
        else:
            break
for j in range(len(li)):
    print(li[j])
    


