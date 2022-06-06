class Solution(object):
    def jump(self, nums):
        A = len(nums)
        if(A == 1): return 0
        maxD = nums[0]
        ans = 0
        i = 1
        j = nums[0]
        while (i <= j and i < A):
            maxD = max(maxD, nums[i] + i)
            if(i == j or i == A - 1):
                j = maxD
                ans += 1
            i += 1
        return ans
