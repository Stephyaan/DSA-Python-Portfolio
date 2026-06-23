'''A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. 
Some applications of this data structure include auto-complete and spell checker systems.Implement the PrefixTree class:
PrefixTree() Initializes the prefix tree object.
void insert(String word) Inserts the string word into the prefix tree.
boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.'''
'''algorithm:
create function for TrieNode:
    create hash map children, to store children of each node
    set endOfWord to map if end reached
to insert:
    start from root node
    for each char in word:
        check if char not in curr node's children:
            then add it to children of cur char in map
        else, move to next children of cur char
        set endOfWord to True
to search:
    start from root node
    go through each char in word,and for each:
        if char not mapped to children:
            return false
        char mapped to children,then move through children
    return false else
to find prefix:
    start from root
    go through each char in word:
        if char not mapped to any in children:
            return false
        move through next char in childre
    return True
'''
#https://chatgpt.com/s/t_6a3aeb1619588191bb0a8f96118c79c2
#https://chatgpt.com/s/t_6a3aeaf36ac4819191da5384b87ad029
#Trie->prefix tree
#prefix tree->prefixes can be searched efficiently
#StartsWith,search->with starting,

#create trieNode
class TrieNode:
    def __init__(self):
        self.children={} #store children pf each char
        self.endOfWord=False #so to stop

class PrefixTree:
    def __init__(self):
        #initialize data structure here
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        #inserts a word into the trie
        cur=self.root

        for c in word: #through each char in word
            if c not in cur.children: #c not added to tree yet
                cur.children[c]=TrieNode() #make c next child
            
            cur=cur.children[c] #c alrdy added;set cur char=next char from children
        
        cur.endOfWord=True #every char,c, in word looked->out of loop:end

    def search(self, word: str) -> bool:
        #returns if the word is in the trie
        cur=self.root

        for c in word:
            if c not in cur.children:
                return False #a char of word not found in children
            
            cur=cur.children[c] #found->go through children for next

        return cur.endOfWord #reached endOfWord;endOfWord=true->return so shows word found
        
    def startsWith(self, prefix: str) -> bool:
        #returns if there is any word in trie starts with given prefix
        cur=self.root

        for c in prefix: #each char in prefix
            if c not in cur.children:
                return False

            cur=cur.children[c] #move to children

        return True #cant return endOfWord;neednt reach end to see if start substring present 
#time:O(n) length of word
#space:O(t) total trie nodes created in trie
        
