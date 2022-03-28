import sys
ran = int(sys.stdin.readline())
stack = []
for i in range(ran):
    num = int(sys.stdin.readline())
    stack.append(num) if num != 0 else stack.pop()
print(sum(stack))       
    
        
    