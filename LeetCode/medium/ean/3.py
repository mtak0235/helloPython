class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        left = right = 0
        chars = set()
        while right < n:
            if s[right] not in chars:
                chars.add(s[right])
                max_length = max(right - left + 1, max_length)
            else:
                while s[right] != s[left]:
                    chars.remove(s[left])
                    left += 1
                left += 1
            right += 1
        return max_length
