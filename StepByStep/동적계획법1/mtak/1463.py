import sys
n = int(sys.stdin.readline())
a = [0, 0]
for i in range(2, n + 1):
    a.append(a[i - 1] + 1)
    if i%3 == 0:
        a[i] = min(a[i//3] + 1, a[i])
    if i % 2 == 0:
        a[i] = min(a[i//2] + 1, a[i])
print(a[n])