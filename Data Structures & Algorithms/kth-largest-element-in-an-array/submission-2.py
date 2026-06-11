class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap=[]  #to store k largest elements
        for n in nums:
            heapq.heappush(minheap,n) #push each element

            if len(minheap)>k: #when len of heap>k;pop the pushed val
                heapq.heappop(minheap)

        return minheap[0]  #since sorted;smallest in k largest is first element
    '''The heap always stores the k largest elements seen so far.
    Whenever more than k elements exist, the smallest among them is removed.
    Thus, after processing all elements:
    Heap contains exactly the k largest elements.
    Among these k elements:
    smallest = k-th largest overall'''
        