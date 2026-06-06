'''You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.
Algorithm:
if tree empty return result empty list
initialise a queue,q, and append the root to queue
while queue is not empty:
      initially set rightmost element, rightSide, to None 
      go through each node in queue in range len(queue):
           pop the leftmost node 
           update rightSide with node
           append the left child of node to queue,then right child,if exists
      after each level, append rightSide value to result
return result
           
'''
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            qLen=len(q)
            rightSide=None
            for i in range(qLen):
                node=q.popleft()
                if node:
                    rightSide=node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res

#Time:O(n)
#space:O(n)
