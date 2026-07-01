class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        i=0
        while i < len(strs):
            key = str(sorted(strs[i]))
            anagrams.setdefault(key, [])
            anagrams[key].append(i)
            i+=1
        
        return_array = []
        for key in anagrams.keys():
            anagram_subset_array = []
            for index in anagrams[key]:
                anagram_subset_array.append(strs[index])
            return_array.append(anagram_subset_array)
        
        return return_array
        
            