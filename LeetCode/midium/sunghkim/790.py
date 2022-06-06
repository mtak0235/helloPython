class Solution(object):
    def numTilings(self, n):
        if n == 1 or n == 2:
            return n
        if n == 3:
            return 5
        DP = [0] * n
        DP[0] = 1
        DP[1] = 2
        DP[2] = 5
        for i in range(3, n):
            DP[i] = ((DP[i - 1] * 2) + DP[i - 3]) % 1000000007
        print(DP)
        return DP[-1]
        
