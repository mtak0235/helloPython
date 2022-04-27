class Solution(object):
    def fib(self, n):
        if n <= 1: return n
        DP = [0] * (n + 1)
        DP[0], DP[1] = 0, 1
        for i in range(2, n + 1):
            DP[i] = DP[i - 1] + DP[i - 2]
        return DP[n]
