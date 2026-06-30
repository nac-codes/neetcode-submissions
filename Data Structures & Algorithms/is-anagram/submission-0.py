class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_cache_s = {}

        for c in s:
            if c in char_cache_s:
                char_cache_s[c] = char_cache_s[c] + 1
            else:
                char_cache_s[c] = 1
        
        char_cache_t = {}

        for c in t:
            if c in char_cache_t:                
                char_cache_t[c] = char_cache_t[c] + 1
            else:
                if c not in char_cache_s:
                    return False
                char_cache_t[c] = 1

        for key in char_cache_t:
            if char_cache_t.get(key) != char_cache_s.get(key):
                return False
            
        
        return True