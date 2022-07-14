# 가장 긴 팰린드롬 부분 문자열

class Solution:
    def longestPalindrome(self, s: str) -> str: # 시간초과
        def is_pelin(strs: str) -> bool:
            for i in range((len(strs)//2)):
                if strs[i] != strs[-(i+1)]:
                    return False
            return True
    
        for i in range(len(s)-1, -1, -1):
            start = 0
            while start + i < len(s):
                if is_pelin(s[start:start + i+1]):
                    return(s[start:start + i+1])
                start += 1

    def longestPalindrome2(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
    
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result



