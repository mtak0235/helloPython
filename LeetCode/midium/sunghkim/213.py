class Solution(object):
    def rob(self, nums):
        A = len(nums)
        if A <= 3: return max(nums)
        if A == 4: return max(nums[0] + nums[2], nums[1] + nums[3])
        DP1 = [0] * (A - 1)
        for i in range(1, A):
            DP1[i - 1] = nums[i]
        for i in range(2, A - 1):
            if i == 2:
                nums[i] += nums[i - 2]
                DP1[i] += DP1[i - 2]
                continue
            nums[i] += max(nums[i - 2], nums[i - 3])
            DP1[i] += max(DP1[i - 2], DP1[i - 3])
        print(nums, DP1)
        return max(nums[A - 2], nums[A - 3], DP1[A - 2], DP1[A - 3])
