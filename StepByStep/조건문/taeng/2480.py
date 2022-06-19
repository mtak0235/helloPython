# https://www.acmicpc.net/problem/2480
# 2020-06-06 10:19
# 2020-06-06 10:39

s = [int(n[0]) for n in input().split()]

if (cnt := len(set(s))) == 1:
	print(10000 + s[0] * 1000)
elif cnt == 3:
	print(max(s) * 100)
else:
	n = [_n for _n in s if s.count(_n) == 2][0]
	print(1000 + n * 100)
