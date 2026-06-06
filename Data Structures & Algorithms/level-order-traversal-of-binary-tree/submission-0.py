# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs for level-by-level traversal
        res=[] #store result
        q=collections.deque() #initialize queue in python
        q.append(root)

        while q: #q not null
            qLen=len(q)
            level=[]  #sublists initialised
            for i in range (qLen): #each element of queue
                node=q.popleft() #each element from queue popped from left to right
                if node: #while q has elements
                    level.append(node.val)  #sublist appended
                    q.append(node.left) #if left, then add for next level
                    q.append(node.right)
            if level:#no level;then null;neednt
                res.append(level)
        return res



        
