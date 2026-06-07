# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #preorder
        def dfs(node,maxVal): #to compare each node with max
            if not node:
                return 0
            #res=1 initial;root present
            res=1 if node.val>=maxVal else 0 
            maxVal=max(maxVal,node.val)
            #1+left+right 
            res+=dfs(node.left,maxVal) #dfs on next left
            res+=dfs(node.right,maxVal) #dfs on next right
            return res

        return dfs(root,root.val)  #if root, then first maxVal=root
            

        
        
