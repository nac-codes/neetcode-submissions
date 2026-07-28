class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        M = max(e for _, e in intervals)

        starts = [0] * (M + 1)
        ends   = [0] * (M + 1)
        for s, e in intervals:
            starts[s] += 1
            ends[e]   += 1

        result, count, start = [], 0, None
        for i in range(M + 1):
            if count == 0 and starts[i] > 0:
                start = i
            count += starts[i] - ends[i]
            if count == 0 and start is not None:
                result.append([start, i])
                start = None
        return result