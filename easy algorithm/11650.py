import sys
a = int(sys.stdin.readline());coordinates =[]
for i in range(a):
    coordinates.append(list(map(int,sys.stdin.readline().split())))
coordinates.sort()
for i in coordinates:
    x_y = ' '.join(list(map(str, i)))
    print(x_y)