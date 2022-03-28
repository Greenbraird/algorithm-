import sys
def top():
    return stack[-1] if stack else -1
a = int(sys.stdin.readline())
stack = []; printer = [];rase = 1 
for i in range(a):
    num = int(sys.stdin.readline())
    while top() < num:
        stack.append(rase)
        rase += 1
        printer.append('+')
    if top() == num:
        stack.pop();printer.append('-')
    elif top() > num and num in stack:
        printer.append('a')
print ('NO')if 'a' in printer else print('\n'.join(printer)) 
