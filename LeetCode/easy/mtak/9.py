class Solution:
    def isPalindrome(self, x: int) -> bool:
        ret=None
        if x < 0:
            ret = False
        else:
            original = x
            reverse = 0
            while (x):
                remainder = x % 10
                x //=10
                reverse = reverse*10 + remainder
            if reverse == original:
                ret = True
            else:
                ret = False
        return ret
