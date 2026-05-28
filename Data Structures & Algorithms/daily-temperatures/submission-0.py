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