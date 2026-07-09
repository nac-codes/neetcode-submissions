import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            diff = heapq.heappop(heap) - heapq.heappop(heap)
            if diff != 0:
                heapq.heappush(heap, diff)
        
        return -heap[0] if len(heap) > 0 else 0