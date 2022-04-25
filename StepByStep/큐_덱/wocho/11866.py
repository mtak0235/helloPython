from collections import deque
import sys
print = sys.stdout.write

N, K = map(int, input().split())

queue = deque()
for i in range(1, N + 1):
    queue.append(i)

print('<')
for _ in range(K - 1):
    queue.append(queue.popleft())
print(f'{queue.popleft()}')

while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())
    print(f', {queue.popleft()}')

print('>\n')
