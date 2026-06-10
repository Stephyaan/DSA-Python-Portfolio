'''Implement an algorithm to serialize and deserialize a binary tree.
Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across 
a network to be reconstructed later in another computer environment.You just need to ensure that a binary tree can be 
serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on 
how your serialization/deserialization algorithm should work.Note: The input/output format in the examples is the same as how NeetCode 
serializes a binary tree. You do not necessarily need to follow this format.'''
'''Algorithm:
serialize():
create an empty string ser to store node values
define recursive function dfs()
for each node:
     if node is null:
         add "N," to ser
     else add str(node.value)+',' to string
     recursively continue for:
        serialize left subtree
        serialize right subtree
call dfs(root) and return final string ser

deserialize():
split the string data at delimeter ','  to get single nodes values
initialize index variable i=0
define recursive function dfs():
for each char from in string:
    initialize the index pinter i nonlocally
    if "N",:
       increment the index pointer i to move forward
       return as null node
   else add the integer node val to tree
   increment the pointer on string
   recursively compute:
       call first dfs() to add nodes left subtree construct left chile
       then call dfs() to add nodesright subtree
   return the constructed node
call dfs() from 0
return node by dfs this is root

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ser=""

        #string in preorder
        def dfs(node):
            nonlocal ser #need to be referenced as non local
            if not node:
                ser+="N,"  #for empty node, add N to string with delimeter
                return

            ser+=str(node.val)+','  #delimeters required to seperate node values
            dfs(node.left)   #recursively for left subtree
            dfs(node.right)  #recursively for right subtree
            
        dfs(root)   
        return ser[:-1]  #, after last node value need to be removed from final serialized string
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val=data.split(',') #split the ser string at ',' and store as val
        i=0

        def dfs(): #recursively thorugh each val
            nonlocal i #define non locally
            
            #if val is "N" then its null node,
            if val[i]=="N": 
                i+=1  #move to next val position
                return None
            
            #val not null,add node to tree
            node=TreeNode(int(val[i]))  
            i+=1       #move to next node
            node.left=dfs()   #recursively do in left subtree;preorder so next elemnets after root goes to left subtree
            node.right=dfs()   #recursively do then in right subtree
            return node   #return the node
        
        return dfs()   
#time:O(n)
#space:O(n)

            

            
