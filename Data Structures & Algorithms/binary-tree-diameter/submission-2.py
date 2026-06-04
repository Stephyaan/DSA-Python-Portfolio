'''The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. 
The path does not necessarily have to pass through the root.The length of a path between two nodes in a binary 
tree is the number of edges between the nodes. Note that the path can not include the same node twice.
Given the root of a binary tree root, return the diameter of the tree.'''
'''Algorithm
If the tree is empty, return 0.
For each node:
Compute height of its left subtree.
Compute height of its right subtree.
Compute diameter through that node = leftHeight + rightHeight.
Recursively find diameter of left subtree.
Recursively find diameter of right subtree.
The final diameter for this node is the maximum of:
diameter through this node
diameter in left subtree
diameter in right subtree
Return that maximum.'''
sol:
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

#time:O(n^2)
#space:O(n)
