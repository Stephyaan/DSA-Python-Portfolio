#qn: You are given the heads of two sorted linked lists list1 and list2.Merge the two lists into one sorted linked list and return the 
head of the new sorted linked list.The new list should be made up of nodes from list1 and list2.
#Algorithm:
#set dummy to a empty linked list node
#set node ponter, tail , ponting to dummy node
#while the list1 and list2 are not empty loop through each node in lists.
     #compare list1 and list2 values
     #set smaller node to next
     #move the chosen list forward.
#when one list becomes empty, attach the remaining of the other lists to next.node
#return the dummy.next which is head of merged lost
Sol:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy    #tail is pointer pointing to dummy, moves as operations in dummy moves frwd

        while list1 and list2:   #list1 & list2 not empty
            if list1.val < list2.val:
                tail.next=list1     #list.val is next item; so pointer
                list1=list1.next    #increment list1 item to next in list1
            else:
                tail.next=list2    #list2 item smaller, so its next item
                list2=list2.next    #increment list2 item to next item in list2
            tail=tail.next        #tail will be ponting to the next in tail

        if list1:
            tail.next=list1    #if not emptied, add to tail
        elif list2:
            tail.next=list2
        return dummy.next       #return dummy.next=head of dummy

#time O(n+m)
#space:O(1)
        
