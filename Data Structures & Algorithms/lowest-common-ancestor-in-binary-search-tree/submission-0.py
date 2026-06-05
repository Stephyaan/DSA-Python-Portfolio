# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #starts from root;further curr comsidered as root
        curr=root
        
        while curr: #curr not null
           #in bst;greater val in right;so gets p&q by moving right
            if p.val>curr.val and q.val>curr.val:
                curr=curr.right
            #p&q less than root;so in left so moving left
            elif p.val<curr.val and q.val<curr.val:
                curr=curr.left
            #neednt move,found node where seperates
            else:
                return curr
        