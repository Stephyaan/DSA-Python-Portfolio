'''Given a binary tree, return true if it is height-balanced and false otherwise.
A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.'''
'''Algorithm:
if root is null return true(balanced=0)
compute leftdepth and rightdepth for left subtree Nand right subtree
if abs(leftdepth-rightdepth) > 1 , return false
check if 
    left subtree balanced
    right subtree balanced
return true if all checks passed as balanced
'''
sol:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        leftHeight=self.maxDepth(root.left)
        rightHeight=self.maxDepth(root.right)

        if abs(leftHeight-rightHeight) > 1 :
            return False
        else :
            return self.isBalanced(root.left) and self.isBalanced(root.right)
            #checking repeatedly for each subtree if balanced/not
    

    def maxDepth(self,root:Optional[TreeNode])->int:
        if not root:
            return 0
        leftDepth=self.maxDepth(root.left)
        rightDepth=self.maxDepth(root.right)

        return 1+max(leftDepth,rightDepth)

#time:O(n^2)
#space:O(n)
