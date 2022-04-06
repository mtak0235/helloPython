N = int(input())

time = list(map(int, input().split()))
time.sort()

ans = 0
wait = 0
for i in range(len(time)):
    wait += time[i]
    ans += wait

print(ans)
