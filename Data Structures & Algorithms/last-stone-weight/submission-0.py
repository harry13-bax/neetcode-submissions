class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        self.heap=stones
        heapq.heapify(self.heap)
        while len(self.heap)>1:
            first=-heapq.heappop(self.heap)
            second = -heapq.heappop(self.heap)
            if first!=second:
                heapq.heappush(self.heap,-(first-second))
        if self.heap:
            return -self.heap[0]
        return 0 