# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen=set()   #to add the elemnts 
        curr=head
        while curr:
            if curr in seen:
                return True  #cycle possible only if val in list alrdy
            seen.add(curr)   #not in set,1st time appearing in 
            curr=curr.next
        return False