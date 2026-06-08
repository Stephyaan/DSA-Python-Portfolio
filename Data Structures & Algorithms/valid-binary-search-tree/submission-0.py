# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node,left,right):
            if not node:
                return True
            
            if not (left<node.val<right): #invalid binary tree;not satisfy
                return False
            
            #valid(nodes,left,right)
            #to check the subtrees of each child too with parents
            #recursively chack validity for all nodes with its left and right values
            return (valid(node.left,left,node.val) #curr left val;left boundary,parent/existingprev/ root
            and 
            valid(node.right,node.val,right)) #curr right val,parent/existing/prev root, right boundary
        
        return valid(root,float("-inf"),float("inf")) #root can be btwn -infinity and plus infinity initially