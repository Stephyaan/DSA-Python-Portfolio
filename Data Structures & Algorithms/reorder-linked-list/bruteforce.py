#You are given the head of a singly linked-list.The positions of a linked list of length = 7 for example, can intially be represented as:
[0, 1, 2, 3, 4, 5, 6]. Reorder the nodes of the linked list to be in the following order:[0, 6, 1, 5, 2, 4, 3]
Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:[0, n-1, 1, n-2, 2, n-3, ...]
You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
#Algorithm:
#Traverse the linked list and push every node into an array called nodes.
#Initialize two pointers:
#i = 0 (start)
#j = len(nodes) - 1 (end)
#While i < j:
#Link nodes[i].next to nodes[j]; increment i.
#If i >= j, break the loop.
#Link nodes[j].next to nodes[i]; decrement j.
#After the loop, set nodes[i].next = None to terminate the list.
#The reordered list is constructed in-place.
sol:
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

#Time:O(n)
#space:O(n)

        
