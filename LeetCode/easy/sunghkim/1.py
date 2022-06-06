class Solution(object):
    def twoSum(self, nums, target):
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                S = nums[i] + nums[j]
                if (S > target): continue;
                if (S == target): return([i,j])
