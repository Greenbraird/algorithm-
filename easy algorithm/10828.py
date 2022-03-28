import sys
def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    return 0 if stack else  1

def top():
    return stack[-1] if stack else -1

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
    elif order == 'top':
        print(top())
    

