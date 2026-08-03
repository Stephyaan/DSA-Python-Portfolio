class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cnt = 0
        prevEnd = intervals[0][1] #1st interval end took as prevend

        #from next interval take its start and end
        for start, end in intervals[1:]: 
            #if start is greater than the end of prev-dif range
            if start >= prevEnd: 
                prevEnd = end 
            else:
                cnt += 1 #else comes in one range
                prevEnd = min(end, prevEnd) 
        return cnt