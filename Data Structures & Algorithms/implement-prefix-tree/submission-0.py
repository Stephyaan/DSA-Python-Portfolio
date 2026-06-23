#create trieNode
class TrieNode:
    def __init__(self):
        self.children={} #store children pf each char
        self.endOfWord=False #so to stop

class PrefixTree:
    #prefix tree->prefixes can be searched efficiently
    #StartsWith,search->with starting,

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
        
        