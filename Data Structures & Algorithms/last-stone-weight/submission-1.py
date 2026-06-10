class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #multply every val with -1 as maxHeap not in Python
        stones=[-s for s in stones]
        heapq.heapify(stones)  #Heap

        while len(stones)>1 :   #stones not alrdy left with 1 stone 
            first=heapq.heappop(stones)  #first heaviest
            second=heapq.heappop(stones)  # second heaviest

            if second > first:  #new weight
                heapq.heappush(stones,(first-second))

        stones.append(0)  #if len stones not > 1; no stones left, need to return 0
        return abs(stones[0])  #return final stone weight left
