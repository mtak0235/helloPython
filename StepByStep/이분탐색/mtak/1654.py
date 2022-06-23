import sys
input = sys.stdin.readline
k, n = map(int, input().split())
a =[int(input()) for _ in range(k)]

low = 1
high = max(a)
ret = 0
while low <= high:
    mid = (low + high) // 2
    cnt = 0
    for i in range(k):
        cnt += a[i]// mid
    if cnt >= n:
        low = mid + 1
        if ret < mid:
            ret = mid
    else:
        high = mid - 1
print(ret)
