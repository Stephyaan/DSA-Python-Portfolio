'''Given the root of a binary tree, return its depth.The depth of a binary tree is defined as the number of nodes
along the longest path from the root node down to the farthest leaf node.
Example 1:Input: root = [1,2,3,null,null,4] ; Output: 3
'''
'''Algorithm:
Check root and if root null ; return 0
Else compute depth recursively:
    left depth as maxDepth(root.left)
    right depth as maxDepth(root.right)
return 1+max(leftDepth,rightDepth) as the max depth of tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 #cant be None
            'next return works only if int here;None cant work on max()'
        
        #leftDepth = maxDepth(root.left)
        #rightDepth=maxDepth(root.right)
        #return 1+max(leftDepth,rightDepth)
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

#time:O(n) ; n=no. of nodes
#space:O(h) ; h=height
       #balanced tree:O(logn) - best case
       #degenerate tree:O(n) - worst case
