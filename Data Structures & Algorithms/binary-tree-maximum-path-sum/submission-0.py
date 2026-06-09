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