'''Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a 
value greater than the value of node x Given the root of a binary tree root, return the number of good nodes within the tree.'''
'''Algorithm:
start dfs from root and store max value so far in mavVal
if root null,return 0
initialise res=1 if node>=maxVal,count as goodnode ,else 0
update max value with max value so far
recursively check:
   left child with maximum value
   right child with updated max
sum up count of good nodes on left and on right
return res
'''
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
            
             #1+left+right 
            res=1 if node.val>=maxVal else 0 #res=1 initial;root present
            maxVal=max(maxVal,node.val)
           
            res+=dfs(node.left,maxVal) #dfs on next left
            res+=dfs(node.right,maxVal) #dfs on next right
            return res

    #time:O(n)
    #space:O(n)

        return dfs(root,root.val)  #if root, then first maxVal=root
            

        
        
