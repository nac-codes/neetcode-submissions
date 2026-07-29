class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval
        if not intervals:
            return [[ns,ne]]

        i = 0
        while i < len(intervals):
            s, e = intervals[i]
            # print(s, e, i)
            # print(ns, ne)
            # print(intervals)
            if ns > e: # new interval is greater than current
                i += 1
                # print("ns > e")
                if len(intervals) == i:
                    intervals.append([ns,ne])
                    break
                continue
             # new interval is less than current

            if ne < s:
                intervals.insert(i, [ns, ne]) 
                # print("ne < s")
                break               

            # if ns or ne are within the current index, then we have a problem
            # if s <= ns <= e or s <= ne <= e:
            # print("s <= ns <= e")
            intervals[i] = [min(s, ns), max(e, ne)]
            if i < len(intervals)-1:
                ns, ne = intervals[i+1]
                intervals.pop(i+1)                    
            else:
                break
            
            
        return intervals
