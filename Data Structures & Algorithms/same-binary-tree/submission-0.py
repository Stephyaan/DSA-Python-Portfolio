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

        