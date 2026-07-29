class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        delta = defaultdict(int)
        for s, e in intervals:
            delta[s] += 1
            delta[e] -= 1
        
        result = []
        count = 0
        start = None
        for i in sorted(delta):
            if count == 0:
                start = i
            count += delta[i]
            if count == 0:
                result.append([start, i])
        
        return result