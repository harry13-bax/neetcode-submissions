class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap=[]
        for x,y in points:
            dist=math.sqrt(x**2+y**2)
            heapq.heappush(self.heap,[dist,x,y])
        res=[]
        while k>0:
            dis,x,y=heapq.heappop(self.heap)
            res.append([x,y])
            k-=1
        return res

        