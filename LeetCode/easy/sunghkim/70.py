class Solution(object):
    def climbStairs(self, n):
        DP = [0] * n
        if n <= 3:
            return n
        DP[0] = 1; DP[1] = 2 ; DP[2] = 3
        for i in range(3, n):
            DP[i] = DP[i - 1] + DP[i - 2]
        return DP[-1]
