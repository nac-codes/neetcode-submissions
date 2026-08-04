class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        delta = defaultdict(int)

        for start, end in intervals:
            delta[start] += 1
            delta[end] -= 1
        
        count, result, start = 0, [], None
        for key in sorted(delta):
            if count == 0:
                start = key
            count += delta[key]
            if count == 0:
                result.append([start, key])
        
        return result

            