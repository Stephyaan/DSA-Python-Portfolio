class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]

        for i in range(len(intervals)):

            #look if newInterval smaller than 1st interval
            if (newInterval[1]<intervals[i][0]):
                res.append(newInterval) #since smaller, added 1st
                return res+intervals[i:] #remaining alrdy larger intervals added
            
            #new interval larger than those in list
            elif (newInterval[0]>intervals[i][1]):
                res.append(intervals[i])

            #new not larger/smaller but overlapped;then newInterval updated
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]

        #append the newInterval if its updated(overlapped)
        res.append(newInterval)
    
        return res