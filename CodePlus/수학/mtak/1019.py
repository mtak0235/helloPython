import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
result = [0 for _ in range(10)]
point = 1
start = 1
end = int(input())
def second(t):
    while t > 0:
        result[t%10] += point
        t//=10

while start <= end:
    while end % 10 != 9:
        second(end)
        end -= 1
    if end < start:
        break
    while start % 10 != 0:
        second(start)
        start += 1
    start //= 10
    end //= 10
    for i in range(10):
        result[i] += (end - start + 1) * point
    point *= 10

for i in result:
    print(i, end=' ')
print()
