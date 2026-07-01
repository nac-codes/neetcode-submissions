class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        i=0
        while i < len(strs):
            count = [0] * 26
            for c in strs[i]:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
                        
            anagrams.setdefault(key, [])
            anagrams[key].append(strs[i])
            i+=1
        
        return_array = []
        for key in anagrams.keys():            
            return_array.append(anagrams[key])
        
        return return_array
        
            