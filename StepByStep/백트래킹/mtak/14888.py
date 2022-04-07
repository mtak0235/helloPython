import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
s = list(map(int, input().split()))
_max = 1000000000 + 1
_min = -1000000000 - 1

def dfs(p,m,mu, di, cnt, sum):
    global _max
    global _min
    global n
    if cnt == n:
        _max = max(_max, sum)
        _min = min(_min, sum)
    if p > 0:
        dfs(p - 1, m, mu, di, cnt + 1, sum + a[cnt])
    if m > 0:
        dfs(p, m - 1, mu,di, cnt + 1, sum - a[cnt])
    if mu > 0:
        dfs(p, m, mu - 1, di, cnt + 1, sum * a[cnt])
    if di > 0:
        dfs(p, m, mu, di - 1, cnt + 1, sum // a[cnt])
dfs(s[0], s[1], s[2], s[3], 1, a[0])
print(_max)
print(_min)

