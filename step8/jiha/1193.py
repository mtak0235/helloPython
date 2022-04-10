# 수학 문제 싫어
n = int(input())

l = 0
s = 0
for i in range(1, 10000000):
    s += i
    if s >= n:
        l = i
        break
s = s - i + 1

if l % 2 == 1:
    print(l -(n - s), end='')
    print('/', end='')
    print(1 + n - s, end='')
else:
    print(1 + n - s, end='')
    print('/', end='')
    print(l -(n - s), end='')