class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #to check dup
        res=[]
        
        def backtrack(i,subset):
            if i==len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i]) #append to subset
            backtrack(i+1,subset) #move to next
            subset.pop() #remove from subset recent

            #no dups whrn list end not reached
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1  #dup found;next element
            backtrack(i+1,subset) #recur fn


        backtrack(0,[]) #start from start
        return res