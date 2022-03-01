import sys

n, m = map(int, sys.stdin.readline().split())
_input = list(map(int, sys.stdin.readline().split()))
_sum = 0
_ret = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            _sum = _input[i] + _input[j] + _input[k]
            if _sum <= m and _sum > _ret:
                _ret = _sum
print(_ret)
