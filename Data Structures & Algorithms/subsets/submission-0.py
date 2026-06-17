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

            