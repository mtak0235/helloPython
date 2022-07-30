class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = 0
        for i in range(len(nums)):
            if (nums[i] != val):
                nums[new] = nums[i]
                new += 1
        return (new)