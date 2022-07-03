class Solution(object):
    def romanToInt(self, s):
        a = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ret = 0
        if len(s) == 1:
            return a[s[0]]
        n = s[1]
        for i in range(len(s) - 1):
            if a[s[i + 1]] > a[s[i]]:
                ret -= a[s[i]]
            else:
                ret += a[s[i]]
        ret += a[s[-1]]
        return ret
        
