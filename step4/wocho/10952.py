import sys

input = sys.stdin.readline

lst = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    lst.append(str(a + b))
print('\n'.join(lst))