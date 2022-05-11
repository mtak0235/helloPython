import numpy as np

class Solution(object):
    def sortedSquares(self, nums):
        lst = np.array(nums)
        lst = lst * lst
        result = lst.sort()
        return (lst)
        
