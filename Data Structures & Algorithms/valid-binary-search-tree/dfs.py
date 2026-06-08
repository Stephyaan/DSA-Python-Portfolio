'''Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.
A valid binary search tree satisfies the following constraints:
The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.'''
'''Algorithm:
start dfs from root between range -infinity to +infinity
if root null,return True(empty tree)
for each node,check if lies between left and right boundary:
     else return false
recursively for each node:
    validate left subtree with updated range(left,node.val)
    validate right subtree with updated range(node.val,right)
if all nodes satisy this range, valid bst,returns True
'''
sol:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node,left,right):
            if not node:
                return True
            
            if not (left<node.val<right): #invalid binary tree;not satisfy
                return False
            
            #valid(nodes,left,right)
            #to check the subtrees of each child too with parents
            #recursively chack validity for all nodes with its left and right values
            return (valid(node.left,left,node.val) #curr left val;left boundary,parent/existingprev/ root
            and 
            valid(node.right,node.val,right)) #curr right val,parent/existing/prev root, right boundary
        
        return valid(root,float("-inf"),float("inf")) #root can be btwn -infinity and plus infinity initially

#time:O(n)
#space:O(1)
