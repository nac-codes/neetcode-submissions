import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while (r>l and r>0 and l<len(s)):
            while s[r].isalnum() == False and r>0 and l<len(s):
                r-=1
            while s[l].isalnum() == False and r>0 and l<len(s):
                l+=1
            if s[r].lower() != s[l].lower():
                return False
            r-=1
            l+=1
         
        return True
            