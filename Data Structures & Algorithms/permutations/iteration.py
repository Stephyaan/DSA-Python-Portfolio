'''Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.
Example 1: Input: nums = [1,2,3] ; Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]'''
'''algorithm:
create firstly perms=[[]]
for each num in nums:
    create a empty [],new_perm
    for every permutation p in perms:
        create copy of new_perm
        Insert num into every index 0..len(p) to create new permutations (add every elemnt to every position of each copy to create new permutation)
        append each copy to perms
    set perms=new_perm
return final perms
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[[]]
        
        for n in nums:
            new_perm=[]
            for p in perms:
                for i in range(len(p)+1):
                    copy_perm=p.copy() #copy of each perms to later add the element
                    copy_perm.insert(i,n) #insert i element in all perm start;with all element
                    new_perm.append(copy_perm)
            perms=new_perm
        return perms
                
   #time:O(n!* n^2)
    #space:O(n!*n)
https://chatgpt.com/s/t_6a345e9bd70c8191a499cbbc3fb61ecb



                
