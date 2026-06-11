'''Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
Follow-up: Can you solve it without sorting?'''
'''algorithm:
create a minHeap to store elements of nums
iterate through each element in nums:
    add them to minHeap
    when lenght of minHEap goes beyond k, stop
    pop out eleemnts one by one from minHeap
the last top element in minHeap is the root, kth largest element.
return the value
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        return heapq.nlargest(k,nums)[-1]
#time:O(n*log k)
#space:O(k)
