# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes=[]

        for lst in lists:  #each of k lists,lst, in main LinkedList, lists,are added together to one array
            while lst:
                nodes.append(lst.val) #each of k list value(node value of main linked list) added to array
                lst=lst.next  #next lst in lists
        nodes.sort()   #sort finally obtained all values from all lists

        result=ListNode(0)  #Linked List to store result
        curr=result   #pointer to point next node pos in resulting LInked list
        for n in nodes:  #loop through each element in nodes array
            curr.next=ListNode(n)  #in result array,add each element as node
            curr=curr.next    #move pointer to next node positon

        return result.next  #return each node form result Linked List


