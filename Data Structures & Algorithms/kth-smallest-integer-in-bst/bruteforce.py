'''Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.
A binary search tree satisfies the following constraints:
The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.'''
'''Algorithm:
initialise an empty array to store nodes
traverse by dfs:
   append the node value to the array
   traverse through the left subtree and insert node values to array as elements
   traverse the right subtree and append node values to arr
sort the array
return the kth smallest element
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
            
            #returns the array with all node elements
            arr.append(node.val)#nodes appended
            dfs(node.left) #start with left subtree;smallest nodes
            dfs(node.right) #then start with right subtree;greater nodes

        #start traversing from root
        dfs(root)
        arr.sort() #nodes are sorted in array
        return arr[k - 1] #return kth smallest element 
      
  #time:O(nlogn) sorting-logn and traversing
    #space:O(n)
        
