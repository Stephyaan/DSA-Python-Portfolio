'''Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.
For a word to be present it must be possible to form the word with a path in the board with horizontally 
or vertically neighboring cells. The same cell may not be used more than once in a word.'''
'''Algorithm
Build a Trie from all words.
Each Trie node stores children (next letters) and isWord (true if a word ends here).
Initialize:
    res as a set (to avoid duplicates).
    visit as a set for the current DFS path.
Define DFS dfs(r, c, node, wordSoFar):
    If (r,c) is out of bounds, already visited, or board[r][c] is not in node.children, stop.
    Mark (r,c) visited.
    Move Trie pointer: node = node.children[board[r][c]]
    Append current char to wordSoFar.
    If node.isWord == true, add wordSoFar to res.
    Recurse to 4 neighbors (up/down/left/right) using the updated node and wordSoFar.
    Backtrack: remove (r,c) from visit.
Run DFS starting from every cell (r, c) with the Trie root.
Return all collected words from res.'''

class TrieNode:
    def __init__(self):
        self.children={}
        self.isWord=False

    def addword(self,word):
        cur=self    
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.isWord=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            root.addword(w)

        Rows,Cols=len(board),len(board[0])
        res,visit=set(),set()

        def dfs(r,c,node,word):
            if(r<0 or c<0 or
                r>=Rows or c>=Cols or
                (r,c) in visit or board[r][c] not in node.children):
                return

            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.isWord:
                res.add(word) #set so add()

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c)) #set so remove()
        
        for r in range(Rows):
            for c in range(Cols):
                dfs(r,c,root,"")
#time : O(m*n*4*3^t-1 +s)
        #space:O(s)

        return list(res)


            

