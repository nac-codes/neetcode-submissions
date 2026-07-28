class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        delta = defaultdict(int)
        for s, e in intervals:
            delta[s] += 1
            delta[e] -= 1
        
        result = []
        count = 0
        cur_start = None
        for x in sorted(delta):
            if count == 0:
                cur_start = x
            count += delta[x]
            if count == 0:
                result.append([cur_start, x])
        
        return result
