'''Design a data structure that supports adding new words and searching for existing words.Implement the WordDictionary class:
void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter. '''
'''Algorithm: 
Add Word:
Start at the root node.
For each character in the word:
    If the character is not present in the current node's children, create a new Trie node.
    Move to the corresponding child node.
After processing all characters, mark the last node as the end of a word.
End.

Search Word (Supports . Wildcard): 
Start searching from the root node and the first character of the word.
For each character:
    If the character is a normal letter:
        If it is not found in the current node's children, return False.
        Otherwise, move to the corresponding child node.
    If the character is .:
        Recursively search every child node for the remaining part of the word.
        If any recursive search returns True, return True.
        If none succeed, return False.
After processing all characters:
Return True if the current node is marked as the end of a word.
Otherwise, return False.
'''
#https://chatgpt.com/s/t_6a3bd2ce10648191972416c50fc3a807
class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root

        for c in word: #each char in word
            if c not in cur.children: #if not in children add to children as node
                cur.children[c]=TrieNode()
            
            cur=cur.children[c] #if c found in childre, take its values next
        cur.word=True #last word added->true

    def search(self, word: str) -> bool:
        def dfs(j, root): #cur index,cur trie node
            cur = root #root

            for i in range(j, len(word)): #from cur index every char looked
                c = word[i] #set cur char c
                
                #if . ->  it can match any child
                if c == ".": #if . it can match any child
                    for child in cur.children.values(): #recursively look for matching child
                        if dfs(i + 1, child): 
                            return True #match child found->true
                    return False
                
                #cur char is normal char
                else:
                    if c not in cur.children: #if no matching in children->false
                        return False
                    cur = cur.children[c] #matched in children->go through each char next
            
            #after all char,end->true if this char is end of word
            return cur.word 

        return dfs(0, self.root)

#time:O(n) for add() and O(n) for search
#space:O(t+n) t=trienodes created, n=length of word
