'''Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, 
return the lowest common ancestor (LCA) of the two nodes.The lowest common ancestor between two nodes 
p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.'''
'''Algorithm:
set curr=root
while curr not null
  if p.val and q.val less than the curr.val; move left
  if p.val and q.val greater than curr.val; move right
  else then found the node where seperates first;the LCA; return curr
return null if tree is empty(no return)
'''
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

#time:O(h) height of tree
#space:O(n) LCA node space
