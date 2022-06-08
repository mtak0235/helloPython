# https://www.acmicpc.net/problem/1193
# 분수찾기
# 2022-06-08 09:01
# 2022-06-08 09:22 
# 시간초과!!!


def pattern(X: int, _max: int, _add: int) -> int:
	n = 1
	for x in range(1, X):
		if n == 1:
			if _add == -1:
				_max += 2
				_add = 1
				continue
		elif n == _max:
			_add = -1
		n += _add
	return n


X = int(input())
a, b = pattern(X, 1, -1), pattern(X, 2, 1)
print(f"{a}/{b}")
