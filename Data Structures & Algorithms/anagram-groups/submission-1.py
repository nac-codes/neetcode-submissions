class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        i=0
        while i < len(strs):
            str_signature = {}
            for c in strs[i]:
                if c in str_signature.keys():
                    str_signature[c] = str_signature[c]+1
                else:
                    str_signature[c] = 1
            key_signature = ""
            for key in sorted(str_signature.keys()):
                key_signature += key + str(str_signature[key])
            # key = str(sorted(strs[i]))
            anagrams.setdefault(key_signature, [])
            anagrams[key_signature].append(strs[i])
            i+=1
        
        return_array = []
        for key in anagrams.keys():            
            return_array.append(anagrams[key])
        
        return return_array
        
            