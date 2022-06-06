import sys
input = sys.stdin.readline

N = int(input())

ans = []
for _ in range(N):
    num = int(input())
    dp = list()
    dp.append((1, 0))
    dp.append((0, 1))
    for i in range(2, num + 1):
        dp.append((dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]))
    ans.append(f'{dp[num][0]} {dp[num][1]}')

print('\n'.join(ans))
