import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
start = 1 
end = K

while start <= end:
    mid = (end+start)//2
    cnt = 0
    for i in range(1,N+1):
        cnt += min(mid//i,N)
    if cnt >= K:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1  
print(ans)
