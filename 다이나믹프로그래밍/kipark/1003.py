#[1003] 백트래킹, 피보나치 함수 kipark
import sys

dp = [0, 1] + [0] * 100

for i in range(2, dp):
	dp[i] = dp[i-2] + dp[i-1]

print

