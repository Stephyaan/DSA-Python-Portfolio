# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight=self.maxDepth(root.left) #max left depth
        rightHeight=self.maxDepth(root.right) #max right depth
        sub=leftHeight+rightHeight #sums to get path length
        diam=max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))  #path length set as diameter 
         #diam set as max in current and prev computed diam

        return max(diam, sub) #return final max diameter

    #max depth to left+right sums to largest path from one end to other
    def maxDepth(self,root:Optional[TreeNode])->int:

        if not root:
            return 0

        leftDepth= self.maxDepth(root.left) #depth with left node as root
        rightDepth= self.maxDepth(root.right) #depth with right node as root
        return 1+max(leftDepth,rightDepth) #return max depth 