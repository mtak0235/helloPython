import sys
input = sys.stdin.readline
cases = int(input())
for i in range(cases):
    clothes = int(input())
    m = {}
    for j in range(clothes):
        t, n = input().strip().split()
        if n in m:
            m[n].append(t)
        else:            
            m[n] = [t]
    cnt = 1
    for p in m:
        cnt *= (len(m[p]) +1)
    print(cnt - 1)       
