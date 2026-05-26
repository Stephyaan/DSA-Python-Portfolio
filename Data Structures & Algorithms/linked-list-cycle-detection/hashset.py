#qn: Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. 
If index = -1, then the tail node points to null and no cycle exists.Note: index is not given to you as a parameter.
#algorithm:
#create empty hash set, seen, to add elements encountered.
#start from head
#loop through list while node is not null
     #if curr node is in set already, cycle possible,return True
     #else add the element to the hash set
#move the next node forward
#if reached null, no cycle found, return False 
sol:
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

#time:O(n)
#space:O(n)
