class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0

        diffs = {}
        while i < len(nums):

            diff = target - nums[i]

            if diff in diffs:
                return [diffs[diff],i]            
            
            diffs[nums[i]] = i
            i +=1
        
        return []
