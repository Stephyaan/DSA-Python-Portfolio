#Qn: Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.
#algrithm:
#Traverse the linked list and push every node into an array.
#Compute the index of the node to remove: len(nodes) - n.
#If this index is 0, it means the head must be removed → return head.next.
#Otherwise, connect nodes[removeIndex - 1].next to nodes[removeIndex].next.
#Return the updated head.
sol:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=[]
        curr=head
        while curr:
            dummy.append(curr)
            curr=curr.next
        removeIndex=len(dummy)-n
        if removeIndex==0:        #head removed 
            return head.next
        dummy[removeIndex-1].next=dummy[removeIndex].next  #next of prev node of removeIndex node is node next to removeIndex node.
        return head                                        #so removeIndex node not there.prev connected to its next

#time:O(n)
#Space:O(n)
