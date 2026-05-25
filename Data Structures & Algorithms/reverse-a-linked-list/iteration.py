#qn: Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
#algorithm:
#initialise: prev=none, curr=head
#while curr exists:
    #set temp=curr.next
    #curr.next=prev
    #prev=curr
    #curr=temp
#return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr=None,head

        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

#time:O(n)
#space:O(1)
