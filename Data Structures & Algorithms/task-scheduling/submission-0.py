class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #most freq task first minimize idle time
        #maxheap not in python;so use neg minHeap;pop smallest (smallest neg) which wld be larget (non negg
    
        count=Counter(tasks)   #Counter(tasks)->hashMap built-in python
        maxHeap=[-cnt for cnt in count.values()]  #maxHeap to store freq of char
        heapq.heapify(maxHeap)
        
        time=0
        q=deque()  #pairs of [-cnt,idleTime] ; queue for more organized 
        while maxHeap or q:
            time+=1
            if maxHeap: #not empty then need to pop 
                cnt=1+heapq.heappop(maxHeap)  #check if cnt(freq= 0;then neednt push to queue
                if cnt:
                    q.append([cnt,time+n]) #cnt exist; so push freq&time req

            if q and q[0][1] == time: #time of any in q matches current time; pop from q and push that to maxHeap
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
#here log 26;still time:O(n)
#maxHeap in Time=O(logn)