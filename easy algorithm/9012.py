import sys
def discri(x):
    sum = 0
    for i in x:
        if i == '(':
            sum += 1
        elif sum == 0 and i == ')':
            return 'NO'
        elif i == ')':
            sum -= 1
    return 'YES' if sum == 0 else 'NO'
a = int(sys.stdin.readline())
for _ in range(a):
    print(discri(sys.stdin.readline()))

