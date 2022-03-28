while True:
    a = list(map(int,input().split()))
    if a == [0 ,0 ,0]:
        break
    elif a.pop(a.index(max(a)))**2 == a[0]**2 + a[1]**2:
        print("right")
    else:
        print('wrong')