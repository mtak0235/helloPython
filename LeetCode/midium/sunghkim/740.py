class Solution(object):
    def deleteAndEarn(self, nums):
        DP = [0] * 10001
        cnt = 0
        for i in nums:
            if DP[i] == 0: cnt += 1
            DP[i] += i
        if cnt == 1:
            return DP[nums[0]]
        N = 0
        if DP[1] != 0:
            N = 1
        for i in range(2, 10001):
            if N == cnt:
                break
            if DP[i] != 0: N += 1
            DP[i] = max(DP[i - 1], DP[i] + DP[i - 2]) 
            DP[0] = max(DP[0], DP[i])
        return DP[0]
        
