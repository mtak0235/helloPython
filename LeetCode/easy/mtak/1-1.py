from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            hash = {nums[i] : i for i in range(len(nums))}
                    for i in range(len(nums)) :
                                c = target - nums[i]
                                            if hash.get(c, False) and hash.get(c, False) != i:
                                                            return [i, hash.get(c)]

                                                            s = Solution()
                                                            tmp = [2, 7, 11, 15]
                                                            if __name__ == '__main__':
                                                                print(s.twoSum(tmp , 9))

