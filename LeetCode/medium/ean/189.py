from math import gcd

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k %= n
        def rotate_i(nums, k, start_index):
            first = nums[start_index]
            dst, src = start_index, start_index + n - k
            while src != start_index:
                nums[dst] = nums[src]
                dst, src = src, (src + n - k) % n
            nums[dst] = first

        if k == 0:
            return ;
        for i in range(gcd(n, k)):
            rotate_i(nums, k, i)
