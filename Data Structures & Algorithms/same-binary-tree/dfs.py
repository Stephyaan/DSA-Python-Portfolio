'''Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.'''
'''Algorithm
check if both are null, return true
if any one null, return false
if both null, and values of p and q are equal
recursively compare 
    with p.left and q.left
    with p.right and q.right
return true only if both subtrees comparisons are equal
'''
sol:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #equal trees
            return True
        
        #p not null, q not null, values of p&q equal
        if p and q and p.val==q.val: #recursively perform for the subtrees
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else: #if fails
            return False
#time:O(n^2)
#space:O(n)
        
