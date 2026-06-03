You are given the root of a binary tree root. Invert the binary tree and return its root.
Example 1: Input: root = [1,2,3,4,5,6,7] ;; Output: [1,3,2,7,6,5,4]
'''Algorithm
If the current node is null, return null.
Swap the node's left and right pointers.
Recursively call dfs on the new left child.
Recursively call dfs on the new right child.
Return the current node (now inverted).
'''
sol:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        #swap left and right ; works for all level of children
        tmp=root.left
        root.left=root.right
        root.right=tmp
        'root.left,root.right=root.right,root.left'  #same as swapping

        
        self.invertTree(root.left) #calls left node of root->as root,and performs swapping
        self.invertTree(root.right) #calss right node of root->as root, and performs swapping
        return root

#time:O(n)
#space:O(n) for rescursion stack
