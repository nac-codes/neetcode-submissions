class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        result = 0
        prev = float('-inf')

        for s, e in intervals:
            if s < prev:
                result += 1
            else:
                prev = e           
        
        return result