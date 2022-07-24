n, *l = list(map(int, open(0).read().strip().split("\n")))
if n <= 2:
	print(sum(l))
else:
	dp = [0] * len(l)
	dp[0] = l[0]
	dp[1] = l[0] + l[1]
	dp[2] = max(dp[1], max(l[0], l[1])+l[2])
	for i in range(3, len(l)):
		dp[i] = max(dp[i-1], dp[i-2]+l[i], dp[i-3]+l[i-1]+l[i])
	print(dp[-1])
