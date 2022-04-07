import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()

ans = []
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        ans.append(queue.popleft() if queue else '-1')
    elif command[0] == 'size':
        ans.append(str(len(queue)))
    elif command[0] == 'empty':
        ans.append('0' if queue else '1')
    elif command[0] == 'front':
        ans.append(queue[0] if queue else '-1')
    elif command[0] == 'back':
        ans.append(queue[-1] if queue else '-1')

print('\n'.join(ans))
