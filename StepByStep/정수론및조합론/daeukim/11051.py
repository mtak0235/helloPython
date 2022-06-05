# 이항 계수 2
from math import factorial
n, k = map(int, input().split())
result = factorial(n) // (factorial(k) * factorial(n - k))
print(result % 10007)