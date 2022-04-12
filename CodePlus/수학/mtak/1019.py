import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
result = [0 for _ in range(10)]
def second(t):
    while t > 0:
        result[t%10] += 1
        t = t//10

def first(n):
    global result
    if n == -1:#얼마나 멀리?
        return
    first(n - 1)
    second(n)

first(int(input()))
for i in result:
    print(i, end=' ')
print()
