# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        array=[]
        curr=head
        while curr:
            array.append(curr.val)
            curr=curr.next

        for i in range(0, len(array), k):
            if ((i + k) <= len(array)):
                array[i:i+k] = array[i:i+k][::-1]

    
        res=ListNode(0)
        curr=res
        
        for i in array:
            curr.next=ListNode(i)
            curr=curr.next
        
        return res.next

#time: O(n)
#space: O(n)


