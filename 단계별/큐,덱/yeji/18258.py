#[18258]큐덱,큐2

import sys
from collections import deque

n = int(sys.stdin.readline()) #몇번 수행?
q = deque([])

for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        if not q: 
            print(-1) #큐에 정수가 없으면 -1출력
        else:
            print(q.popleft())
    elif s[0] == 'size':#큐의 개수 출력
        print(len(q)) 
    elif s[0] == 'empty': #큐가 비어있으면 1, 아니면 0을 출력
        if not q: 
            print(1)
        else:
            print(0)
    elif s[0] == 'front': #큐의 가장 앞의 정수 출력, 없으면 -1출력
        if not q:
            print(-1)
        else:
            print(q[0])
    elif s[0] == 'back': #큐의 가장 뒤의 정수 출력, 없으면 -1출력
        if not q:
            print(-1)
        else:
            print(q[-1])