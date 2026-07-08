import heapq

class KthLargest:
    # top_k = []

    def __init__(self, k: int, nums: List[int]):
        self.top_k = heapq.nlargest(k, nums) #descending
        self.k = k
        # print(self.top_k)

    def add(self, val: int) -> int:
        if len(self.top_k) == 0:
            self.top_k.append(val)
            return val
        
        index = None
        for i, n in enumerate(self.top_k):
            if val >= n:
                index = i
                break 
    
        if index is not None:            
            self.top_k.insert(index, val)
            if len(self.top_k) > self.k:
                self.top_k.pop()


        return self.top_k[-1]
