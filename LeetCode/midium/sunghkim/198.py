class Solution(object):
    def rob(self, nums):
        A = len(nums)
        if A <= 2: return max(nums)
        nums[2] += nums[0]
        for i in range(3, A):
            nums[i] += max(nums[i - 2], nums[i - 3])
        return max(nums[A - 1], nums[A - 2])
