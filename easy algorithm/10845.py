import sys
def pop():
    return -1 if(not stack) else stack.pop(0) 

def size():
    return len(stack)

def empty():
    return 0 if stack else  1

def front():
    return -1 if(not stack) else stack[0]

def  back():
    return -1 if(not stack) else stack[-1]
    

num = int(sys.stdin.readline())
stack = []
for i in range(num):
    input_split = sys.stdin.readline().rstrip().split()
    order = input_split[0]
    if order == 'push':
        stack.append(input_split[1])
    elif order == 'pop':
        print(pop())
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    elif order == 'front':
        print(front())
    elif order == 'back':
        print(back())