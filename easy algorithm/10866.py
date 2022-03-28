import sys
def push_front():
    
    return stack.insert(0,input_split[1])

def push_back():
    return stack.append(input_split[1])

def pop_front():
    return -1 if(not stack) else stack.pop(0)

def pop_back():
    return -1 if(not stack) else stack.pop()

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
    if order == 'push_front':
        push_front()
    elif order == 'push_back':
        push_back()
    elif order == 'pop_front':
        print(pop_front())
    elif order == 'pop_back':
        print(pop_back())    
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    elif order == 'front':
        print(front())
    elif order == 'back':
        print(back())