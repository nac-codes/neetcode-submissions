class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in range(len(nums), 0, -1):
            freq_map[n] = []
    
        freq = {}
        for e in nums:
            if e in freq.keys():
                freq[e] += 1
            else:
                freq[e] = 1
        
        for e in freq.keys():
            freq_map[freq[e]].append(e)
        
        return_array = []
        for f in freq_map.keys():
            freq_array = freq_map[f]
            if len(freq_map[f]) > 0:
                for e in freq_array:
                    if len(return_array) >= k:
                        return return_array
                    return_array.append(e)
        
        return return_array
