import sys
input = sys.stdin.readline

a = [1, 1, 1, 2, 2]
cnt = int(input())

def p(n):
    if (len(a) < n):
        for i in range(len(a), n):
            a.append(a[i - 1] + a[i - 5])
    return a[n - 1]

for _ in range(cnt):
    g = int(input())
    print(p(g))
