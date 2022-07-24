class Solution:
    def isPalindrome(self, x: int) -> bool:
        converted_int = str(x);
        for i in range(len(converted_int)):
            if (converted_int[i] != converted_int[len(converted_int) - 1 - i]):
                return (False);
        return (True);
        