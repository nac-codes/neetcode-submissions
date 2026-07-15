class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = [[] for _ in range(len(nums) + 1)]
    
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num, freq in counts.items():
            freq_map[freq].append(num)
        
        return_array = []
        for i in range(len(nums), 0, -1):            
            for num in freq_map[i]:                    
                if len(return_array) >= k:
                    return return_array
                return_array.append(num)
        
        return return_array
