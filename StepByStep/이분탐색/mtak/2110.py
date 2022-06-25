import sys
input = sys.stdin.readline
n, c = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])
start = 1
end = a[-1] - a[0]
res = 0
while start <= end:
    mid = (start + end) // 2
    old = a[0]
    cnt = 1
    for i in range(1, n):
        if a[i] >= old + mid:
            cnt += 1
            old = a[i]
    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)
