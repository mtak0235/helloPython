class Solution(object):
    def numDecodings(self, s):
        A = len(s)
        DP = [0] * A
        for i in range(A):
            if i == 0 and s[i] != '0':
                DP[i] = 1
                continue
            if i != A - 1 and s[i + 1] == '0':
                DP[i] = DP[i - 1]
                continue
            if s[i] == '0':
                if i == 0 or s[i - 1] == '0' or int(s[i - 1]) > 2: return 0
                else: DP[i] = DP[i - 1]
                continue
            tmp = (int(s[i - 1]) * 10) + int(s[i])
            if 10 < tmp and tmp < 27: 
                if i != 1:  DP[i] = (DP[i - 1] + DP[i - 2])
                else:       DP[i] = 2
            else: DP[i] = DP[i - 1]
        print(DP)
        return (DP[-1])
        
        
