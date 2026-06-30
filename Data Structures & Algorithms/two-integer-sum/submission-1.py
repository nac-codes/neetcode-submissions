class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        j = 0
        breaker = False

        while i < len(nums):
            j=i+1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    breaker = True
                    break
                j+=1
            
            
            if breaker:
                break
            
            i+=1

        return([i,j])
