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
            node.left=dfs()   #recursively do i left subtree
            node.right=dfs()   #recursively do in right subtree
            return node   #return the node
        
        return dfs()    

            

            
