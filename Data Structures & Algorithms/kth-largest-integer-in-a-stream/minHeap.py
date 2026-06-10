'''Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. 
The stream is not necessarily sorted. Implement the following methods:
constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.'''
'''Algorithm
Initialization():
Insert all initial numbers into a min-heap.
If the heap size becomes greater than k, repeatedly remove the smallest element.
After this, the heap contains exactly k elements.

add(value):
Insert the new value into the min-heap.
If heap size > k:
Remove the smallest element (the heap root).
Return the heap's smallest element (the root), which is now the k-th largest.
'''
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

#time:O(m*logk) ; m=no.of times add() called
#space:O(k)
