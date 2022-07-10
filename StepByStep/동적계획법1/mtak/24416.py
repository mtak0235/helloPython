import sys
input = sys.stdin.readline
cnt = int(input())
f = [None] * 50
f[1] = f[2] = 1


def fib(n):
    if n == 1 or n == 2:
        return 1  # 1
    else:
        return (fib(n - 1) + fib(n - 2))


def fibonacci(n):
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]  # 2
    return f[n]


count1 = fibonacci(cnt)
count2 = cnt - 2
print(count1, count2)
