class Solution(object):
    def tribonacci(self, n):
        if n == 0: return 0
        if n <= 2: return 1
        DP = [0] * (n + 1); DP[0] = 0; DP[1] = 1; DP[2] = 1
        for i in range(3,n + 1):
            DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]
        return DP[-1]
