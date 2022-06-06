import sys
from collections import deque
input = sys.stdin.readline
g = int(input())
a = deque([_ for _ in range(1,g + 1)])
while len(a) > 1:
    a.popleft()
    t = a.popleft()
    a.append(t)
print(a[0])