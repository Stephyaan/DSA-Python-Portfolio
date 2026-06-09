'''Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. 
A node can not appear in the sequence more than once. The path does not necessarily need to include the root.
The path sum of a path is the sum of the node's values in the path.'''
'''Algorithm:
Maintain a global result res, initialized with the root’s value.(to store max path sum)
Define dfs(node):
    If node is None, return 0.
    Recursively compute:
        leftMax = dfs(node.left)
        rightMax = dfs(node.right)
    Ignore negative downward paths: (prevent negative sum)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)
    Update global result with the best path through node:
    res = max(res, node.val + leftMax + rightMax)  (update the max path sum to new max path sum)
    Return the best "extendable" downward path:
        node.val + max(leftMax, rightMax)           ( return the best max path sum)
Call dfs(root) and return res.
'''
sol:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #max path stored in res[]
        res=[root.val]  #max path would be root for non-empty bst

        def dfs(root):
            if not root:
                return 0

            #traversing through root recursively
            leftMax=dfs(root.left) #set leftMax as left child from root
            rightMax=dfs(root.right) #rightmax as next right child

            leftMax=max(leftMax,0) #if leftmax neg.,drop it;compared with 0
            rightMax=max(rightMax,0) #if rightMax sum neg,drops it and chnaged to 0
            
            #update maxSum res array with new max path sum
            res[0]=max(res[0],(root.val+leftMax+rightMax))
            return root.val+ max(leftMax,rightMax) #return best max downward path

        dfs(root)
        return res[0]

#time:O(n)
#space:O(n)
