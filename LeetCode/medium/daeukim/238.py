# 자신을 제외한 배열의 곱
# 나눗셈을 하지 않고 O(n)에 풀이

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= p
            p *= nums[i]
        return out
