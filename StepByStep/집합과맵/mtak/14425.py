import sys
input = sys.stdin.readline
n, m = map(int, input().split())
N = set()
for _ in range(n):
    N.add(input().strip())
cnt = 0
for _ in range(m):
    if input().strip() in N:
        cnt += 1
print(cnt)
