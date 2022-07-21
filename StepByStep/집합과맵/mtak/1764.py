import sys
input = sys.stdin.readline
n, m = map(int,  input().split())
f = set([input().strip() for _ in range(n)])
s =set([input().strip() for _ in range(m)])
res =f & s
print(len(res))
for p in sorted(res):
    print(p)
