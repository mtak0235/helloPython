N = int(input())

dp = list()
dp.append(0)
dp.append(1)
dp.append(2)

for i in range(3, N + 1):
    dp.append((dp[i - 2] + dp[i - 1]) % 15746)

print(dp[N])
