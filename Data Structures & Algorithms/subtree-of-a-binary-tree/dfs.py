'''Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure
and node values of subRoot and false otherwise.A subtree of a binary tree tree is a tree that consists of a node in tree and 
all of this node's descendants. The tree tree could also be considered as a subtree of itself.
'''
'''Algorithm:
If subRoot is empty → return true (empty tree is always a subtree).
If root is empty but subRoot is not → return false.
At the current root node:
      If sameTree(root, subRoot) is true, return true.
Recursively check:
      isSubtree(root.left, subRoot)
      isSubtree(root.right, subRoot)
Return true if either side returns true.

sameTree(root1, root2):
If both nodes are null → return true.
If only one is null → return false.
If values differ → return false.
Recursively check left children and right children.
'''
sol:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: #empty tree always subtree
            return True
        if not root: #subtree present but root empty(not present), False
            return False
        if self.sameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

    def sameTree(self,root:Optional[TreeNode],subRoot:Optional[TreeNode])->bool:
        if not root and not subRoot: #equal trees->both empty
            return True

        if root and subRoot and root.val==subRoot.val:
            return (self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right))
        
        return False

#Time:O(m*n)
#space:O(m+n)
