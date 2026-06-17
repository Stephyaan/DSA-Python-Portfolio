'''Given an array nums of unique integers, return all possible subsets of nums.
The solution set must not contain duplicate subsets. You may return the solution in any order.Example 1:
Input: nums = [1,2,3] ; Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]'''
'''algorithm:
create res array to store subsets
initialize a subset array
define a recurring function dfs(i):
    if i equals len(nums):
        add the copy of subset to res array
        return
    if choice1-to add element to subset:
        append to subset array
        recurse to next index (call dfs(i+1) with next index)
    if choice2-not to add element to subset:
        (pop the recently added from subset)
        recurse to next index (call dfs(i+1) with next index)

start recursion from start index dfs(0)
return the res array
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #idea and concept of decision tree
        #decision tree starts from 1st element
        res=[]

        subset=[] #subset to be modified

        #decision tree starts from 1st element
        def dfs(i):  #i=cur element visiting
            #i>=len(nums) out of bound->append copy of subset to res
            if i>=len(nums):  
                res.append(subset.copy())
                return  

            #decision to append nums[i] to subset
            subset.append(nums[i])
            dfs(i+1)    #move to next element->given to it a subset with element at i

            #decision to not include nums[i]
            subset.pop()  #pop from subset recently appended->not added
            dfs(i+1)  #move to bext element->given to it empty subset
        
        dfs(0) #start from start 
        return res
#time:O(n*2^n)    2^n subsets 
#space: O(2^n) for output array
#O(n) extra space
