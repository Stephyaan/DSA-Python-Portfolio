'''algorithm:
create a minHeap to store dist
for each point in points list:
    compute the distance=x^2+y^2
    store [dist,x,y] as heap entry
create a minheap with all these entries using heapify
create array res to store k closest points
repeat k times: (while k>0)
    pop the smallest point from minHeap
    append [x,y ]it to res array
    (move k pointer to k-=1)
return res array
'''
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

#time:O(n+k∗logn) when building the heap with heapify, or O(n∗logn+k∗logn) when inserting each point with a heap push.
#Space complexity: O(n)1)
