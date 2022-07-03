import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
ret = 0
low = 0
high = max(a)
while low <= high:
    mid = (high + low) // 2
    left = 0
    for i in a:
        if mid < i:
            left += (i - mid)
    if left >= m:
        low = mid + 1
        if mid > ret:
            ret = mid
    else:
        high = mid - 1
print(ret)
