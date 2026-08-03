class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        #each interval added to res check one by one with all rest
        res=[intervals[0]]

        #through each interval
        for i in range(1,len(intervals)):
            
            #start greater than end of a res interval
            if intervals[i][0]>res[-1][1]:
                res.append(intervals[i])  #not overlapped;different range

            else: #overlapped
                res[-1][1]=max(res[-1][1],intervals[i][1])
        
        return res
