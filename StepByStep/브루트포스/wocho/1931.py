import sys
input = sys.stdin.readline

N = int(input())

time = []
for _ in range(N):
    time.append(tuple(map(int, input().split())))
time.sort(reverse=True)

i = 0
ans = 0
now = float("inf")
while i < len(time):
    if time[i][0] <= now and time[i][1] <= now:
        ans += 1
        now = time[i][0]
    i += 1

print(ans)
