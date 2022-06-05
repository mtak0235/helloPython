import sys
input = sys.stdin.readline
cnt = int(input())
while cnt:
    cnt-= 1
    g = input().strip()
    t = list()
    res = 'YES'
    for i in g:
        if i == '(':
            t.append(i)
            continue
        if len(t) == 0:
            res = 'NO'
            break
        t.pop()
    if len(t) != 0:
        res = 'NO'
    print(res)
