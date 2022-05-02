class Solution(object):
    def canJump(self, nums):
        A = len(nums)
        DP = [0] * A
        DP[0] = 1
        
        def pull(i, j):
            for k in range(i, j + 1):
                DP[k] = 1
        
        for i in range(A):
            print(i, DP[i])
            if DP[i] == 0: return False
            if i + nums[i] >= (A - 1): return True
            if DP[i + nums[i]] == 1: continue
            pull(i + 1, i + nums[i])
        if DP[-1] == 1: return True
        return False
