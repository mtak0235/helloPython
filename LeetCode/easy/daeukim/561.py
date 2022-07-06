# 배열 파티션 1
# O(nlog n)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans
    
    def arrayPairSum2(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

