import math

t = int(input())
result = []

for _ in range(t):
    h, w, n = map(int, input().split())

    y = h if n % h == 0 else n % h
    x = math.ceil(n / h)

    result.append(y * 100 + x)


for i in range(t):
    print(result[i])