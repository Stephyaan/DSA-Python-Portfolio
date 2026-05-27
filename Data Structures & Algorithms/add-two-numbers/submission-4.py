'''You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.The digits are stored in reverse order, 
e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.Each of the nodes contains a single digit. 
You may assume the two numbers do not contain any leading zero, except the number 0 itself.Return the sum of the two numbers as a linked list.'''
sol:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   #create resulting linked list 
        cur = dummy   #ponter for each node

        carry = 0
        while l1 or l2 or carry:  #while atleast l1 or l2 or carry is not null
            v1 = l1.val if l1 else 0     #take value of l1 node
            v2 = l2.val if l2 else 0     #take value of l2 node

            # new digit
            val = v1 + v2 + carry    #calculate new sum value 
            carry = val // 10      #15->carry is 1
            val = val % 10         #obtain ones place as only single digit possible
            cur.next = ListNode(val)   #set next node value to to ones place digit of sum value

            # update ptrs
            cur = cur.next   #move ponter forward
            l1 = l1.next if l1 else None   #take next node's value from list 1 if not null
            l2 = l2.next if l2 else None   #similarly fro list 2

        return dummy.next   #return list nodes final
 #time :O(max(m,n))  or O(m+n)
#space:O(1), O(max(n,m)
