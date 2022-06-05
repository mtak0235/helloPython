class Solution(object):
    def mySqrt(self, x):
        if (x == 0):
            return (0)
        if (x == 1):
            return (1)
        i = 0
        a = float(x / 2)
        while (i < 30):
            a = (a +(x / a)) / 2
            i += 1;
        return (int(a))