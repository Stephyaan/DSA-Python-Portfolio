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