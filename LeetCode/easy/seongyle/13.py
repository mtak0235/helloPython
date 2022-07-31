class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        doubles = {'CM' : 900, 'CD': 400, 'XC' : 90, 'XL' : 40, 'IX': 9, 'IV' : 4};
        singles = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        i = 0;
        
        while (i < len(s)):
            if (i < len(s) - 1 and s[i:i+2] in doubles):
                sum += doubles[s[i:i+2]]
                i+=2
            else:
                sum += singles[s[i]]
                i+=1
        return (sum);
        