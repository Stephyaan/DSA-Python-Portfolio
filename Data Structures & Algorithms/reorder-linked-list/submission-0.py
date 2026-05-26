# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr=head
        dummy=[]
        while curr:
            dummy.append(curr)
            curr=curr.next
        i=0
        j=len(dummy)-1
        while i<j:
            dummy[i].next=dummy[j]
            i+=1
            if i>=j:
                break
            dummy[j].next=dummy[i]
            j-=1
        dummy[i].next=None
        

        