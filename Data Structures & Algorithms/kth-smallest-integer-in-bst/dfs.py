'''Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.
A binary search tree satisfies the following constraints:
The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.'''
'''algorithm:
create an empty array to store nodes
traverse through dfs:
  traverse through left subtree nodes
  append node.val into the array
  traverse through right subtree nodes
after traversing, resulting array would be sorted
return the [k-1] th element of array for kth smallest node
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
     
        arr = []
        #traversing bst by dfs
        def dfs(node):
            if not node:
                return
            #returns in sorted order
            dfs(node.left) #start with left subtree;smallest nodes
            arr.append(node.val)#nodes appended
            dfs(node.right) #then start with right subtree;greater nodes
        #start traversing from root
        dfs(root)
        return arr[k - 1] #return kth smallest element 

#time:O(n)
#space:O(n) sorting 
