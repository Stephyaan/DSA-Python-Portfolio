'''You are given two integer arrays preorder and inorder.
preorder is the preorder traversal of a binary tree inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.'''
'''Algorithm:
If either array is empty, return null (base case).
Create a root node with the first element of preorder.
Find the index of the root value in inorder (call it mid).
Recursively build the left subtree using preorder[1:mid+1] and inorder[0:mid].
Recursively build the right subtree using preorder[mid+1:] and inorder[mid+1:].
Return the root node.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])  #root in inorder is at mid
        root.left=self.buildTree(preorder[1:(mid+1)],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
#time:O(n^2)
#space:O(n)

        
