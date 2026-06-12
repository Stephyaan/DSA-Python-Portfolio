'''You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.
Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
Return the minimum number of CPU cycles required to complete all tasks.Example 1:
Input: tasks = ["X","X","Y","Y"], n = 2 ; Output: 5
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.'''
'''Algorithm
Count how many times each task appears.
Build a max-heap where each entry is "remaining count" of a task (the higher the count, the higher its priority).
Create an empty queue (FIFO) to store pairs: (remaining_count_after_running, next_available_time).
Set time = 0.
While the heap is not empty or the cooldown queue is not empty:
    Increment time by 1.
    If the heap is not empty:
        Pop the task with the largest remaining count.
        "Run" it once: remaining_count -= 1.
        If remaining_count > 0, push (remaining_count, time + n) into the cooldown queue (it can be used again after n units).
    Check the front of the cooldown queue:
        While the task at the front has next_available_time == time,
        remove it from the queue and push its remaining_count back into the max-heap.
    (Optional optimization)
        If the heap is empty and the cooldown queue is not empty:
        Let next_time be the next_available_time of the front element in the cooldown queue.
        Set time = next_time (fast-forward), then process step 3 again for that time.
When both the heap and cooldown queue are empty, return time as the minimum time required to finish all tasks.'''
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
#time:O(n) n=no.of tasks
#space:O()
