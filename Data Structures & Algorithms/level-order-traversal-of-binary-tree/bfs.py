'''Given a binary tree root, return the level order traversal of it as a nested list, 
where each sublist contains the values of nodes at a particular level in the tree, from left to right.
Example 1:Input: root = [1,2,3,4,5,6,7] ; Output: [[1],[2,3],[4,5,6,7]]
Algorithm:
return empty result list if tree is empty
create a queue to store elements
append root to queue initially
while queue is not empty:
    qlen is the length of queue which is the no.of nodes in same level
    initialise empty level list for addiing same level nodes
    for each element of queue (range qlen):
       pop from the left most node of queue
       append this node to level list
       append the left and right children of the node to queue if exists
    while level list is not empty append it to the result list
return the final result list
'''
SOL:
BFS whwn level-order traversal required
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

#time:O(n)
#space:O(n)
        
