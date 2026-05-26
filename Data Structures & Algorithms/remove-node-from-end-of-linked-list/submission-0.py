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
        if removeIndex==0:
            return head.next
        dummy[removeIndex-1].next=dummy[removeIndex].next  #next of prev node of removeIndex node is node next to removeIndex node.
        return head                                        #so removeIndex node not there.prev connected to its next

#time:O(n)
#Space:O(n)