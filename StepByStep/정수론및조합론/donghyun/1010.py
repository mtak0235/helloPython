import sys

input = sys.stdin.readline
def combi(n, k):
    a = 1
    for _ in range(k):
        a *= n
        n -= 1
    for i in range(k, 0 , -1):
        a //= i
    return a
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(combi(max(a, b), min(a, b)))