class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < 0:
                lo = mid + 1
            else:
                hi = mid
        down_ptr = max(0, lo - 1)
        up_ptr = down_ptr + 1
        for i in range(n):
            nums[i] *= nums[i]
        l = []
        while down_ptr >= 0 and up_ptr < n:
            if nums[down_ptr] < nums[up_ptr]:
                l.append(nums[down_ptr])
                down_ptr -= 1
            else:
                l.append(nums[up_ptr])
                up_ptr += 1
        while down_ptr >= 0:
            l.append(nums[down_ptr])
            down_ptr -= 1
        while up_ptr < n:
            l.append(nums[up_ptr])
            up_ptr += 1
        return l
