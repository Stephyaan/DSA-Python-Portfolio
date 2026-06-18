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
                
                
         


                