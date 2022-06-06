class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check(a, b):
            for i in range(26):
                if mp_1[i] != mp_2[i]:
                    return False
            return True
        
        n_s1, n_s2 = len(s1), len(s2)
        if n_s1 > n_s2:
            return False        
        mp_1, mp_2 = [0] * 26, [0] * 26
        a_code = ord('a')
        for c in s1:
            mp_1[ord(c) - a_code] += 1
        for i in range(n_s1 - 1):
            mp_2[ord(s2[i]) - a_code] += 1
        left, right = 0, n_s1
        while right <= n_s2:
            mp_2[ord(s2[right - 1]) - a_code] += 1
            if check(mp_1, mp_2):
                return True
            mp_2[ord(s2[left]) - a_code] -= 1
            left, right = left + 1, right + 1
        return False
