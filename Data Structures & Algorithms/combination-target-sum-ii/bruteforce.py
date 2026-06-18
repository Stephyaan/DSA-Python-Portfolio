'''You are given an array of integers candidates, which may contain duplicates, and a target integer target. 
Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.
Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.
You may return the combinations in any order and the order of the numbers in each combination can be in any order.'''
'''algorithm:
Sort candidates.
Use a recursive function dfs(i, cur, total):
If total == target, add a copy of cur to the result.
If total > target or i == len(candidates), stop exploring.
Include the current number:
Add candidates[i] to cur.
Recurse with next index i + 1.
Remove the number (backtrack).
Skip duplicates:
Advance index i forward while the next number is the same.
Exclude the current number:
Call dfs(i + 1, cur, total) after skipping duplicates.
Return the result list.
    explain:"sort the list 
    define a recursive function:
        if the cur combination total==target:
            then append combination to curList
        if total>target or index,i, is the last index,len(candidates), then stop 
    add the 
            candidates[i] number to combination
            recurr from i+1
            remove the element 
    check if i+1 < len(candidates) and still if element at i==i+1
            move to next number
        recurr from the next element dfs(i+1,curList,total+nums)
    call the recursion from start dfs(0,[],0)
    return the result"
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res=[]

        def dfs(i,curList,total):
            if total==target:
                res.append(curList.copy())
                return
            

            if (total > target) or (i == len(candidates)):
                return

            curList.append(candidates[i])
            dfs(i + 1, curList, total + candidates[i])
            curList.pop()


            while (i + 1 < len(candidates)) and (candidates[i] == candidates[i+1]):
                i += 1
            dfs(i + 1, curList, total)

        dfs(0,[],0)
        return res
