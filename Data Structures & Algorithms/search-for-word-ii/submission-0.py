'''Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.
For a word to be present it must be possible to form the word with a path in the board with horizontally 
or vertically neighboring cells. The same cell may not be used more than once in a word.'''

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


        return list(res)


            

