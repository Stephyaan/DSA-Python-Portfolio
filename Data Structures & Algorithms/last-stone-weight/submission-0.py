class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #stones not left with only one weight 
        while (len(stones)>1):
            stones.sort()  
            w=stones.pop()-stones.pop() #last 2 elements are heaviest;popped(smashed heaviest)

            if w:    #if not weights means x-y=0 (same as x==y) no need to append 0
                stones.append(w)  #new weight difference updated

        return stones[0] if stones else 0 #return when last one or no element exist
