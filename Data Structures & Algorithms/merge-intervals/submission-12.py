class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        st = sorted(x[0] for x in intervals)
        en = sorted(x[1] for x in intervals)
        out, start, n = [], st[0], len(intervals)
        for j in range(n):
            if j == n - 1 or st[j+1] > en[j]:
                out.append([start, en[j]])
                if j + 1 < n:
                    start = st[j+1]
        
        return out