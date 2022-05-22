import sys
input = sys.stdin.readline
n, k = map(int, input().split())
t = list(map(int, input().split()))
res = [0] * (n + 1)
for _ in range(n):
	res[_ + 1] = res[_] + t[_]
result = []
for _ in range(k,n +1):
	result.append(res[_] - res[_ - k])
print(max(result))
