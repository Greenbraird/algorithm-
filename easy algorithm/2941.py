import math
def is_prime_number(x):
    if x == 1:
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return  0 
    return 1
a= int(input()); sum = 0;
b = list(map(int,input().split()))
for i in range(len(b)):
    sum += is_prime_number(b[i])
print(sum)