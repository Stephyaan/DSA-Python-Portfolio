'''You are given an array of distinct integers nums and a target integer target. Your task is to return a 
list of all unique combinations of nums where the chosen numbers sum to target.
The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of 
each of the chosen numbers is the same, otherwise they are different.
You may return the combinations in any order and the order of the numbers in each combination can be in any order.'''
'''algorithm:
Sort nums so we can stop early when the sum exceeds the target.
Define a recursive function dfs(i, currentList, total):
If total == target:
Add a copy of currentList to the result.
Return.
Loop j from i to end of list:
If total + nums[j] > target, stop the loop (no need to check larger numbers).
Add nums[j] to currentList.
Call dfs(j, currentList, total + nums[j]) (reuse allowed).
Remove last element to backtrack.
Start recursion with dfs(0, [], 0) and return the result.
'''
[https://chatgpt.com/s/t_6a340bfadadc8191984d47065fa38559]
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() #easy to understand if sum>target can stop

        res=[]
        
        #fn to add each element again to see if target reached
        def dfs(i,currentList,total):
            if total==target:
                res.append(currentList.copy()) #append to final res the list of nos. summed to target   
                return

            for j in range(i,len(nums)): #move to next eleemnt when target not reached
                if (total+nums[j])>target: #greater than target then stop
                    return
                currentList.append(nums[j]) #append curr element to list
                dfs(j,currentList,total+nums[j])  
                currentList.pop()

        dfs(0,[],0)  #start from 0 index
        return res

#time:O(2 t/m)
#space:O(t/m)
#t=target,m=min no.of terms
