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
