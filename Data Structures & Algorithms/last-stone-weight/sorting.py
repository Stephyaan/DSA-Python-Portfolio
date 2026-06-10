'''You are given an array of integers stones where stones[i] represents the weight of the ith stone.
We want to run a simulation on the stones as follows:
At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.
Return the weight of the last remaining stone or return 0 if none remain.'''
'''Algorithm:
while the list,stone, has more than one stone weight as element:
    sort the list in ascending order
    pop the last 2 elements after sorting, for heaviest stones
    new weight,w, is pop.stones()-pop.stones()
    if the new weight>0, append the new weight to the list
        (else the two stones were of same weight, neednt append)
if list has element left:
      return stones[0] for the remaining stone weight
else return 0
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #stones not left with only one weight 
        while (len(stones)>1):
            stones.sort()  
            w=stones.pop()-stones.pop() #last 2 elements are heaviest;popped(smashed heaviest)

            if w:    #if not weights means x-y=0 (same as x==y;destroyed) no need to append 0
                stones.append(w)  #new weight updated

        return stones[0] if stones else 0 #return when last one or no element exist
#time:O(n^2 log n)
#space: O(1) or o(n) depending on sorting
