class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        l = list(s)
        def reverse(l, left, right):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left, right = left + 1, right - 1
        word_start = 0
        whitespace_start = 0
        while whitespace_start < n and l[whitespace_start] != ' ':
            whitespace_start += 1
        while word_start < n:
            reverse(l, word_start, whitespace_start - 1)
            word_start = whitespace_start + 1
            whitespace_start = word_start
            while whitespace_start < n and l[whitespace_start] != ' ':
                whitespace_start += 1
        return ''.join(l)
