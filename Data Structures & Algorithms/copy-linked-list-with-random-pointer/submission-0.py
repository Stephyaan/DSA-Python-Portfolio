"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy={None:None}
        
        curr=head
        while curr:
            copy=Node(curr.val) #clone/copy for each node in Linked list given
            oldToCopy[curr]=copy  #the map stores its copy as value for each node
            curr=curr.next      #move node pointer forward

        curr=head
        while curr:
            copy=oldToCopy[curr]   
            copy.next=oldToCopy[curr.next]
            copy.random=oldToCopy[curr.random]
            curr=curr.next

        return oldToCopy[head]


#Time:O(n)
#space:O(n)