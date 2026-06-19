'''You are given an array nums of integers, which may contain duplicates. Return all possible subsets.
The solution must not contain duplicate subsets. You may return the solution in any order. Example 1:
Input: nums = [1,2,1] ; Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]'''
'''algorithm:
sort the nums
define recursion backtrack(i,subset):
    if len(nums)==i:
        add the copy of subset to result array and return it
    add each element to subset
    continue recursion from next position on i+1
    if cur elemennt and next equals then move pointer frwd;i+1(avoid duplicates)
    call recursion on next unique index
start from backtrack(0,[])
return
'''
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

#time O(n * 2^n)
#space: O(2^n)
