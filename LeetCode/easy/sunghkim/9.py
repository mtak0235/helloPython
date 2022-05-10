import sys
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        f = len(x)
        if (f == 1):
            return (True)
        for i in range(int(f / 2)):
	    	if (x[i] != x[f - 1 - i]):
	    		return (False)
        return (True)