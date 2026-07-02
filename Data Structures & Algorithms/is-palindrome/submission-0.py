import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[\W_]', '', s)
        s = s.lower()
        for i in range(len(s)//2,len(s)):
            j = len(s) - i - 1
            if s[i] != s[j]:
                return False
        
        return True
            