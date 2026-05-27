'''You are given the head of a singly linked list head and a positive integer k.You must reverse the first k nodes in the linked list, 
and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.
Return the modified list after reversing the nodes in each group of k.
You are only allowed to modify the nodes' next pointers, not the values of the nodes.'''
'''Algorithm:
Create an empty array.
Traverse the linked list from head node.
Store each node value into the array.
Traverse the array in steps of size k.
For each group:
Check whether k elements exist.
If yes, reverse that group.
If less than k elements remain, leave them unchanged.
Create a dummy node for the new linked list.
Traverse the modified array.
Create new nodes using array values and attach them to the new linked list.
Return the linked list starting after the dummy node.
'''
sol:
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


