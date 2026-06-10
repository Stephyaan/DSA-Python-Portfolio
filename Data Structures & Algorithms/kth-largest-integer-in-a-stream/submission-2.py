class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #minheap with k larget elements
        #member variable for minHeap
        #memeber variable for k=desired size of k assigned to nums
        self.minHeap, self.k = nums, k
        
        #turn minHeap to heap 
        heapq.heapify(self.minHeap)
        
        #len of minHeap>k(size);pop #popping elements after k position(k largest)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
   
    def add(self, val: int) -> int:
        #push val to heap
        heapq.heappush(self.minHeap, val)

        #if len of minHaap>k;
        #len of minHeap>k(size);pop after kth largest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        #return min from minHeap;minHeap[0]
        return self.minHeap[0]