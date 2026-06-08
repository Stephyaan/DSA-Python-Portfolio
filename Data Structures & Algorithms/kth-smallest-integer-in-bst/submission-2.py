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
      