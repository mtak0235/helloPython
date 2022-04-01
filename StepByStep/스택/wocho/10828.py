import sys
input = sys.stdin.readline

stack = []
result = []

N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        stack.insert(0, cmd[1])
    elif cmd[0] == 'pop':
        if stack:
            result.append(stack.pop(0))
        else:
            result.append("-1")
    elif cmd[0] == 'size':
        result.append(str(len(stack)))
    elif cmd[0] == 'empty':
        result.append(str(0 if len(stack) else 1))
    else:
        if stack:
            result.append(stack[0])
        else:
            result.append("-1")


print('\n'.join(result))