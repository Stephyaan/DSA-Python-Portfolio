'''qn: You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. 
If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.'''
'''Algorithm
Let res store the number of days until a warmer temperature.
For each index i:
Start checking from the next day j = i + 1 and count how many steps it takes to find a warmer day.
If a warmer day is found, store the count.
Otherwise, store 0.
Return the result array.
'''
sol:
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        result=[]
        
        #loop through each element from start, then check following elements if any higher
        for i in range(len(temps)):
            count=1 #to move 1 step fwd,cnt=1
            j=i+1 #start checking from i+1=j element for higher

            while j<len(temps):  #need only first element higher than element at i
                
                #if temp at j> temp at i;
                if temps[j]>temps[i]:
                    break #brk loop so again dont increase cnt going on checking next elements
                
                #move fwd in any case
                j+=1
                #j=n,reached final element,nohigher temp,so count=0
                count+=1 #increment count&j even if temp higher found/not
                
            count=0 if j==len(temps) else count
            result.append(count)  #for i'th temp,place count at result i'th place

        return result

#time: O(n^2)
#Space:O(1);O(n) for output
