''' You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, 
which may point to any node in the list, or null.Create a deep copy of the list.The deep copy should consist of exactly n new nodes, each including:
The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.
Return the head of the copied linked list.
In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] 
where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.  '''
'''algotithm: (2 passes done)
Create a hash map oldToCopy, mapping each original node to its copied node.
Include null -> null for convenience.
First pass: iterate through the original list
Create a copy of each node.
Store the mapping in oldToCopy.
Second pass: iterate again
Set copy.next using oldToCopy[original.next].
Set copy.random using oldToCopy[original.random].
Return the copied version of the head using oldToCopy[head].
'''
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
        
        oldToCopy={None:None}  #in null case, return None
        
        curr=head
        while curr:
            copy=Node(curr.val) #clone/copy for each node in Linked list given created in copy
            oldToCopy[curr]=copy  #the map stores its copy as value for each old node
            curr=curr.next      #move node pointer forward

        curr=head
        while curr:
            copy=oldToCopy[curr]      #get copy
            copy.next=oldToCopy[curr.next]  #set next pointer of copy from curr.next
            copy.random=oldToCopy[curr.random]  #set random pointer   
            curr=curr.next   #update the curr pointer to next

        return oldToCopy[head]


#Time:O(n)
#space:O(n)
