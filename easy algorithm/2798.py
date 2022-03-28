N , M = map(int, input().split())

number = list(map(int, input().split()))
x_count = 0
j_count = 0 

for i in number[:len(number)-2]:
    j_count += 1
    j_count = x_count
    for j in number[j_count:len(number)-1]:
        x_count += 1
        for x in number[x_count:] :
            print(i, j ,x)
            
        