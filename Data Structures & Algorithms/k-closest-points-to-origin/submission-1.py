class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        for x,y in points:
            dist=(x**2)+(y**2) #neednt take sq root for correct sorting
            minHeap.append([dist,x,y])

        heapq.heapify(minHeap) #converting to heap
        res=[]
        while k>0:
            dist,x,y=heapq.heappop(minHeap)  #popping last min dist and assign to variables
            res.append([x,y])
            k-=1  #remaining required points
        return res

